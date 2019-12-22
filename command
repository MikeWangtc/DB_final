Start InfluxDB, Kapacitor 
    brew services start influxdb
    brew services start kapacitor
    brew services start telegraf
    influxdb
Path of kapacitor
    /usr/local/opt/kapacitor
Configuration of kapacitor, telegraf, influxdb
    /usr/local/etc

!!!!!Change kapacitor.conf!!!!!
    python program : prog = "/usr/local/bin/python2"
    args = ["-u", <pathOfUDF.py>]
    pathOfKapacitor : PYTHONPATH = "/usr/local/opt/kapacitor/kapacitor/udf/agent/py"
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Command to define the Kapacitor task (cd to the directory of .tick file)
    kapacitor define <taksName> -tick <task.tick>
Start the recording in the background
    kapacitor record stream -task <taksName> -duration 24h -no-wait
Store returned ID as rid
    rid = <returnedID>
Start to generate data
    python <dataGenerator.py>
Access output by ID
    kapacitor list recordings $rid