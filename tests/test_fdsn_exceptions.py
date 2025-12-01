from eida_statistics_aggregator.stat_collection import StatCollection

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


def test_single_log():
    statistics = StatCollection()
    parsed_stat = statistics.parse_logs([logline])
    assert True


def test_net_out_of_bound():
    logline = """
        {
        "clientID": "IRISDMC DataCenterMeasure/2019.136 Perl/5.018004 libwww-perl/6.13",
        "finished": "2020-09-18T00:00:00.758768Z",
        "userLocation": { "country": "US" },
        "created": "2025-09-18T00:00:00.612126Z",
        "bytes": 98304,
        "service": "fdsnws-dataselect",
        "userEmail": null,
        "trace": [
            {
            "cha": "BHZ",
            "sta": "EIL",
            "start": "2025-08-09T00:00:00.0000Z",
            "net": "7P",
            "restricted": false,
            "loc": "",
            "bytes": 98304,
            "status": "OK",
            "end": "2025-08-09T01:00:00.0000Z"
            }
        ],
        "status": "OK",
        "userID": 1497164453
        }
"""
    statistics = StatCollection()
    parsed_stat = statistics.parse_logs([logline])
    assert True
