import os, sys, json, urllib.request
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
def addStaticMap(listMac):
    with open('staticmapArray.json',encoding="utf-8") as f:
        listStaticmap = json.loads(f.readline())
    for x in listMac:
        if x not in listStaticmap:
            listStaticmap.append(x)
    with open('staticmapArray.json','w') as f:
        f.writelines(json.dumps(listStaticmap))
with open('listHost.json',encoding="utf-8") as f:
    listHost = json.loads(f.readline())

for x in listHost:
    fauxapi_host=x
    fauxapi_apikey="PFFAexample02A"
    fauxapi_apisecret="AABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDi"
    try:
        FauxapiLib = PfsenseFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret, debug=True)
        FauxapiLib.use_verified_https = False
        config = FauxapiLib.config_get()
        addStaticMap(config["dhcpd"]["lan"]["staticmap"])
    except:
        print("Khong the login pfsense: " + x)
#Null
for x in listHost:
    fauxapi_host=x
    fauxapi_apikey="PFFAexample02A"
    fauxapi_apisecret="AABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDi"
    try:
        FauxapiLib = PfsenseFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret, debug=True)
        FauxapiLib.use_verified_https = False
        config = FauxapiLib.config_get()
        with open('staticmapArray.json',encoding="utf-8") as f:
            listStaticmap1 = json.loads(f.readline())
        config["dhcpd"]["lan"]["staticmap"] = listStaticmap1
        FauxapiLib.config_set(config)
        FauxapiLib.send_event('interface all reload')
    except:
        print("Khong the login pfsense: " + x)
