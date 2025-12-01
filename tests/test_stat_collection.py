import json

from eida_statistics_aggregator.stat_collection import StatCollection


def test_unparsable_json():
    logline = "not a json line"
    statistics = StatCollection()
    statistics.parse_logs([logline])
    assert True


def test_ok_request():
    logline = """
        {
        "clientID": "IRISDMC DataCenterMeasure/2019.136 Perl/5.018004 libwww-perl/6.13",
        "finished": "2020-09-18T00:00:00.758768Z",
        "userLocation": { "country": "US" },
        "created": "2020-09-18T00:00:00.612126Z",
        "bytes": 98304,
        "service": "fdsnws-dataselect",
        "userEmail": null,
        "trace": [
            {
            "cha": "BHZ",
            "sta": "EIL",
            "start": "1997-08-09T00:00:00.0000Z",
            "net": "GE",
            "restricted": false,
            "loc": "",
            "bytes": 98304,
            "status": "OK",
            "end": "1997-08-09T01:00:00.0000Z"
            }
        ],
        "status": "OK",
        "userID": 1497164453
        }
    """

    statistics = StatCollection()
    statistics.parse_logs([logline])
    assert statistics.nbevents == 1
    stats = json.loads(statistics.to_json())
    assert len(stats["stats"]) == 1
