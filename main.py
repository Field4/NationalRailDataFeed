import os
from dotenv import main

main.load_dotenv('./.env')

username = os.getenv("uname")

print(username)