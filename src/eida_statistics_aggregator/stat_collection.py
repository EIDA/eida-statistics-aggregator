from datetime import datetime
import logging
from eida_statistics_aggregator.eida_statistic import EidaStatistic
import json
import bz2
import mmh3
import magic
from fdsnnetextender import FdsnNetExtender

class StatCollection():
    """
    This object contains a list of EidaStatistics and some metadata related to the aggregation processing
    """

    def __init__(self):
        """
        :var _stats_days is a list of dates concerning the statistics collection. It is used as metadata to estimate month coverage
        _statistics is a dictionary of EIDA Statistics. The key is computed whithEidaStatistic.key()
        """
        self._stats_dates = []
        self._generated_at = datetime.now()
        self._statistics = {}
        self.nbevents = 0
        self.net_extender = FdsnNetExtender()

    def append(self, stat):
        """
        Append an EidaStatistic object into the collection.
        During this process, if there is already a statistic with the same key, they will be merged.
        :param stat is an EidaStatistic instance
        """
        if stat.key() in self._statistics:
            # append
            self._statistics[stat.key()].aggregate(stat)
        else:
            # create new stat
            self._statistics[stat.key()] = stat
        if stat.original_day not in self._stats_dates:
            self._stats_dates.append(stat.original_day)

    def get_days(self):
        """
        Return a list of sorted dates for this collection.
        """
        return sorted(self._stats_dates)

    def to_json(self):
        """
        Dump the object as a dictionary
        """
        return json.dumps(
            {'generated_at': self._generated_at.strftime('%Y-%m-%d %H:%M:%S'),
             'version': __version__,
             'days_coverage': [ d.strftime('%Y-%m-%d') for d in sorted(self._stats_dates) ],
             'aggregation_score': round(self.nbevents/len(self._statistics)),
             'stats': [v for k,v in self._statistics.items()]
             }, default=lambda o: o.to_dict()
        )

    def parse_file(self,filename):
        """
        Parse the file provided in order to aggregate the data.
        Exemple of a line:
        {"clientID": "IRISDMC DataCenterMeasure/2019.136 Perl/5.018004 libwww-perl/6.13", "finished": "2020-09-18T00:00:00.758768Z", "userLocation": {"country": "US"}, "created": "2020-09-18T00:00:00.612126Z", "bytes":
    98304, "service": "fdsnws-dataselect", "userEmail": null, "trace": [{"cha": "BHZ", "sta": "EIL", "start": "1997-08-09T00:00:00.0000Z", "net": "GE", "restricted": false, "loc": "", "bytes": 98304, "status": "OK", "end": "1997-08-09T01:00:00.0000Z"}], "status": "OK", "userID": 1497164453}
    {"clientID": "ObsPy/1.2.2 (Windows-10-10.0.18362-SP0, Python 3.7.8)", "finished": "2020-09-18T00:00:01.142527Z", "userLocation": {"country": "ID"}, "created": "2020-09-18T00:00:00.606932Z", "bytes": 19968, "service": "fdsnws-dataselect", "userEmail": null, "trace": [{"cha": "BHN", "sta": "PB11", "start": "2010-09-04T11:59:52.076986Z", "net": "CX", "restricted": false, "loc": "", "bytes": 6656, "status": "OK", "end": "2010-09-04T12:03:32.076986Z"}, {"cha": "BHE", "sta": "PB11", "start": "2010-09-04T11:59:52.076986Z", "net": "CX", "restricted": false, "loc": "", "bytes": 6656, "status": "OK", "end": "2010-09-04T12:03:32.076986Z"}, {"cha": "BHZ", "sta": "PB11", "start": "2010-09-04T11:59:52.076986Z", "net": "CX", "restricted": false, "loc": "", "bytes": 6656, "status": "OK", "end": "2010-09-04T12:03:32.076986Z"}], "status": "OK", "userID": 589198147}
        """
        # Test if it's a bz2 compressed file
        if magic.from_file(filename).startswith('bzip2 compressed data'):
            logfile = bz2.BZ2File(filename)
        else:
            logfile = open(filename, 'r')
        # Initializing the counters
        line_number = 0
        # What about a nice progressbar ?
        with click.progressbar(logfile.readlines(), label=f"Parsing {filename}") as bar:
            for jsondata in bar:
                line_number += 1
                try:
                    data = json.loads(jsondata)
                except json.JSONDecodeError:
                    logging.warning("Line %d could not be parsed as JSON. Ignoring", line_number)
                logging.debug(data)
                # Get the event timestamp as object
                try:
                    event_date = datetime.strptime(data['finished'], '%Y-%m-%dT%H:%M:%S.%fZ',).date()
                except ValueError:
                    try:
                        event_date = datetime.strptime(data['finished'], '%Y-%m-%dT%H:%M:%SZ',).date()
                    except ValueError:
                        logging.warning("Could not parse date %s", data['finished'])
                        continue
                try:
                    countrycode = data['userLocation']['country']
                except KeyError:
                    logging.warning("No country code found in %s, default to empty string", data['userLocation'])
                    countrycode = ""
                if data['status'] == "OK":
                    for trace in data['trace']:
                        try:
                            # The short network code has to be extended using it's starting year
                            extended_network = self.net_extender.extend(trace['net'], trace['start'][0:10])
                        except ValueError as err:
                            logging.error(err)
                            sys.exit(1)
                        # Make an EidaStatistic object using this NSLC + date + country
                        new_stat = EidaStatistic(date=event_date, network=extended_network, station=trace['sta'], location=trace['loc'], channel=trace['cha'], country=countrycode)
                        # Then push some values in it
                        new_stat.nb_successful_requests = 1
                        new_stat.size = trace['bytes']
                        new_stat.unique_clients.add_raw(mmh3.hash(str(data['userID'])))
                        # Append this stat to the collection
                        self.append(new_stat)
                else:
                    # TODO This is not very DRY but I did'nt figure a better way to do it for now
                    new_stat = EidaStatistic(date=event_date, country=countrycode)
                    new_stat.nb_unsuccessful_requests = 1
                    new_stat.unique_clients.add_raw(mmh3.hash(str(data['userID'])))
                    self.append(new_stat)
        self.nbevents += line_number

    def nbaggs(self):
        return len(self._statistics)
