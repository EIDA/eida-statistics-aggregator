from eida_statistics_aggregator.stat_collection import StatCollection


def test_reproduce_issue():
    logline = """
    {
        "service": "fdsnws-dataselect",
        "userID": 2320080092,
        "clientID": "python-requests/2.32.5",
        "userEmail": null,
        "auth": false,
        "userLocation": {"country": "IT"},
        "created": "2025-11-24T14:55:32.531889Z",
        "trace": [
            {
                "net": "7C",
                "sta": "CS2FF",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7C",
                "sta": "CS2FS",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7C",
                "sta": "SPAOL",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT04A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT06A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT07A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT08A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT09A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT20A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "OK",
                "bytes": 4096
            },
            {
                "net": "4P",
                "sta": "IT27A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "OK",
                "bytes": 3584
            },
            {
                "net": "4P",
                "sta": "IT28A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "OK",
                "bytes": 3584
            },
            {
                "net": "4P",
                "sta": "IT23A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT24A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "OK",
                "bytes": 4096
            },
            {
                "net": "4P",
                "sta": "IT26A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "4P",
                "sta": "IT22A",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "OK",
                "bytes": 4608
            },
            {
                "net": "7P",
                "sta": "P301",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P307",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P308",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P309",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P310",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P311",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P312",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P313",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P314",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            },
            {
                "net": "7P",
                "sta": "P315",
                "loc": "",
                "cha": "HHZ",
                "start": "2025-11-24T14:49:45.879588Z",
                "end": "2025-11-24T14:50:15.879588Z",
                "restricted": false,
                "status": "NODATA",
                "bytes": 0
            }
        ],
        "status": "OK",
        "bytes": 19968,
        "finished": "2025-11-24T14:55:32.835567Z"
    }
    """

    statistics = StatCollection()
    statistics.parse_logs([logline])
    assert len(statistics._statistics) == 5
