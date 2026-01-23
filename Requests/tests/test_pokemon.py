import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2f6761d64823d41e2eb25c6ccaaeb405'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '46671'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER)
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers/46671', headers = HEADER)
    assert response_get.json()['trainer_name'] == 'SepherotH'   
