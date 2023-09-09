import os

from dotenv import main
import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd

main.load_dotenv('./.env')

username = os.getenv("uname")
password = os.getenv("password")

tokenReq = requests.post('https://opendata.nationalrail.co.uk/authenticate',
                         data={'Content-Type': 'application/x-www-form-urlencoded', 'username': username, 'password': password}, )

# print(tokenReq.status_code)

dataTok = json.loads(tokenReq.text)
token = dataTok.get("token")

# print(token)


dataReq = requests.get("https://opendata.nationalrail.co.uk/api/staticfeeds/4.0/ticket-restrictions", headers={'X-Auth-Token': token})

# print(dataReq.status_code)
data = dataReq.text

root = ET.fromstring(data)

# next block found on 'https://saturncloud.io/blog/converting-xml-to-python-dataframe-a-comprehensive-guide/'

data = []
for elem in root:
    row = {}
    for subelem in elem:
        row[subelem.tag] = subelem.text
    data.append(row)
df = pd.DataFrame(data)

# End block

pd.set_option('display.max_columns', None)
print(df)
#