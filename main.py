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

print(tokenReq.status_code)

dataTok = json.loads(tokenReq.text)
token = dataTok.get("token")

print(token)


dataReq = requests.get("https://opendata.nationalrail.co.uk/api/staticfeeds/4.0/ticket-restrictions",headers={'X-Auth-Token':token})

print(dataReq.status_code)
data = dataReq.text
print(data)
root = ET.fromstring(data)

parsedDict = untangle.parse(root)
df = pd.DataFrame(parsedDict)
df
