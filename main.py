import os
from dotenv import main
import requests
import json

main.load_dotenv('./.env')

username = os.getenv("uname")
password = os.getenv("password")

tokenReq = requests.post('https://opendata.nationalrail.co.uk/authenticate', data={'Content-Type':'application/x-www-form-urlencoded','username':username, 'password':password}, )

print(tokenReq.status_code)

data = tokenReq.text
data = json.loads(data)
token = data.get("token")

print(token)


dataReq = requests.post("https://opendata.nationalrail.co.uk/api/staticfeeds/4.0/ticket-restrictions",data={'X-Auth-Token':token})

print(dataReq.status_code)
