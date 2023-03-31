# Server config
SERVER_IP = "192.168.0.100" # server ip
SERVER_PORT = 8001 # server port

# IPTV config
IPTV_LIST_URL = "http://portal.ruiptv.ru/group.m3u" # url to m3u playlist
IPTV_EPG_LIST_IN = [
    "http://programtv.ru/xmltv.xml.gz",
    "http://epg.it999.ru/epg2.xml.gz"
] # url to epg xml.gz
IPTV_EPG_LIST_OUT = "epg.xml" # file name for out cache epg
IPTV_UPD_INTERVAL_LIST = 86400 # update interval for m3u playlist
IPTV_UPD_INTERVAL_EPG = 86400 # update interval for epg

# Movie and tvseries provider API config
PROVIDER_API_URL = "http://127.0.0.1:8001" 