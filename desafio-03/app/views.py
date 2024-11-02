
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
import requests

# Create your views here.
def index(request):
    def translate_data(characters):
        translator = Translator()

        for character in characters:
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
            
        return characters
    
    per_page = int(request.GET.get('per_page', 10))
    page = int(request.GET.get('page', 1))

    url = f'https://last-airbender-api.fly.dev/api/v1/characters?perPage={per_page}&page={page}'

    response = requests.get(url)

    if response.status_code == 200:
        characters = response.json()

        # translate_data(characters)

        context = {
            'characters': characters,
            'page': page,
        }
        
        return render(request, 'pages/index.html', context)
    else:
        return HttpResponse('Error: ', response.status_code)