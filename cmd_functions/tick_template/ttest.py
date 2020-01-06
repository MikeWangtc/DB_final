import  json

def ttest( urldb, argv, log_path ):
    return f"""dbrp "{ urldb }"."autogen"
var data = stream
    |from()
        .measurement('{ argv["measurement"] }')
    |window()
        .period(10s)
        .every(10s)

data
    @tTest()
        .field('{ argv["field"] }')
        .size({ argv["size"] })
        .detector_type('ttest')
        .detector_params('{ json.dumps(argv["params"]) }')
    |alert()
        .id('{ argv["field"] }')
        .crit(lambda: "is_anomaly")
        .log('{ log_path }')
        |influxDBOut()
            .database('{ argv["database"] }')
            .retentionPolicy('autogen')
            .measurement('{ urldb }_alert')
    
data
    |influxDBOut()
        .create()
        .database('{ argv["database"] }')
        .retentionPolicy('autogen')
        .measurement('{ urldb }')

"""
# .tag('hotend', 'a')
# .tag('bed', 'b')
# .tag('air', 'c')