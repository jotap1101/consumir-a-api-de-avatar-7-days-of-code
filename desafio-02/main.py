from googletrans import Translator
import json
import requests

def translate_data(data):
    translator = Translator()

    for character in data:
        try:
            if 'allies' in character and character['allies']:
                character['allies'] = [translator.translate(ally, src='en', dest='pt').text for ally in character['allies']]

            if 'enemies' in character and character['enemies']:
                character['enemies'] = [translator.translate(enemy, src='en', dest='pt').text for enemy in character['enemies']]

            if 'name' in character:
                character['name'] = translator.translate(character['name'], src='en', dest='pt').text

            if 'affiliation' in character:
                character['affiliation'] = translator.translate(character['affiliation'], src='en', dest='pt').text
        except Exception as e:
            print(f"Erro ao traduzir personagem: {e}")

            continue
        
    return data

url = 'https://last-airbender-api.fly.dev/api/v1/characters'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    translated_data = translate_data(data)
    
    print(json.dumps(data, indent=4, ensure_ascii=False))
else:
    print('Error: ', response.status_code)