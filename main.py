import os

import pandas as pd
from dotenv import main
import requests
import json
import xml.etree.ElementTree as ET
import untangle
import pandas as pd

main.load_dotenv('./.env')

username = os.getenv("uname")
password = os.getenv("password")

tokenReq = requests.post('https://opendata.nationalrail.co.uk/authenticate', data={'Content-Type':'application/x-www-form-urlencoded','username':username, 'password':password}, )

#print(tokenReq.status_code)

dataTok = json.loads(tokenReq.text)
token = dataTok.get("token")

#print(token)


dataReq = requests.get("https://opendata.nationalrail.co.uk/api/staticfeeds/4.0/ticket-restrictions",headers={'X-Auth-Token':token})

#print(dataReq.status_code)
data = dataReq.text

root = ET.fromstring(data)

print(root.tag)
print(root.attrib)
print('children:')

for child in root:
    print(child.tag, child.attrib)

print(root[0][3].text,root[0][4].text,root[0][5].text)