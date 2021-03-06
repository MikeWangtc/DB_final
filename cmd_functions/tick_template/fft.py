def fft( urldb, argv, log_path ):
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
        .detector_type('spectral_residual')
        .detector_params('{argv['params']}')
    |alert()
        .id('{ argv["field"] }')
        .crit(lambda: "is_anomaly")
        .log('{ log_path }')
        |influxDBOut()
            .create()
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