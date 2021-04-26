import urllib
import urllib.request
import xml.etree.ElementTree as ET
import json

What_To_Display = 1
url = "http://web.mta.info/status/serviceStatus.txt"

def Status():
    message = SubwayStatus()
    return message

def SubwayStatus():
    with urllib.request.urlopen(url) as response:
         html = response.read()
         response.close()
         message_all = ""
         new_data = []
         if What_To_Display == 1:
             currentStatus = {}
             root = ET.fromstring(html)
             for i in range(2, 7):
                 m = ""
                 ##ent_name = ""
                 if i == 2:
                         m = "Subway_Status"
                 elif i == 3:
                         m = "Bus_Status"
                 elif i == 4:
                         m = "BT_Status"
                 elif i == 5:
                         m = "LIRR_Status"
                 elif i == 6:
                         m = "MetroNorth_Status"
                 for child in root[i]:
                     currentStatus[child[0].text] = child[1].text
                 for k,v in currentStatus.items():
                     new_data.append({"title": k, "status": v})
                 container = {}
                 container['items'] = new_data
                 with open('/config/data/MTA_' + m + '_data.json', 'w') as outfile: json.dump(container, outfile)
                 container = {}
                 new_data = []
                 currentStatus = {}
    return message_all

Status()
