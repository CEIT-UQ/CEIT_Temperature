'''
Created on Nov 22, 2012

@author: deseram
'''
class MQTT:
    database = None
    database2 = None
    database3 = None
    database4 = None
    database5 = None
    threed_pub = None
    client_cosm = "LIB_cosm"
    client_ts = "LIB_ts"
    client_3d = "LIB_3d"
    client_sense = "LIB_sense"
    client_3bpub = "3dPub"
    client_dbcosm = "LIB_databasecosm"
    client_dbts = "LIB_databasets"
    client_db3d = "LIB_database3d"
    client_dbsense = "LIB_databaseSense"
    client_dblib = "LIB_databaseBase"
    server = "130.102.129.171"
    client = "LIB_temp"
    client_sub = "Edittor"
    topic_db = "/LIB/config/level"
    topic_temp = "/LIB/level4/climate_raw"
    topic_3d = "/LIB/3d/data"
    packet = {"id":"11.11.11", "value":0}
    rc = None
    pi_id = None
    