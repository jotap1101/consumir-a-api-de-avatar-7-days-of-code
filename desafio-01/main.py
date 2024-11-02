import json
import requests

url = 'https://last-airbender-api.fly.dev/api/v1/characters'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print('Error: ', response.status_code)