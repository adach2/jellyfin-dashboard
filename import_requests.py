import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv("JELLYFIN_TOKEN")
print(token)
base_url = "http://localhost:8096"

session = requests.Session()
session.headers.update({'Authorization': f'MediaBrowser Token="{token}"'})

import requests
import json
token = "e3869cd28da64aba90c0f926e12ec4a5"
url = 'http://localhost:8096/System/Info'


r = requests.get(url)
print(r)
with open("System-Info.json","w") as jsonfile:
    json.dump(r.json(),jsonfile, indent=4)