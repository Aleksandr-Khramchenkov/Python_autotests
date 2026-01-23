import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f6761d64823d41e2eb25c6ccaaeb405'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

BODY_POKEMON = {
    "name": "Кокатель",
    "photo_id": 90
}


BODY_POKEMON_NAME = {
    "pokemon_id": "1296816",
    "name": "Котях",
    "photo_id": 90
}


BODY_POKEMON_POKEBALL = {
    "pokemon_id": "1296816"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMON)
print(response.text)

response  = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_POKEMON_NAME)
print(response.text)

response  = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_POKEMON_POKEBALL)
print(response.text)
