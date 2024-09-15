import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6ca1289e4839f842e1117f3e78717d60'
HEADER = {'Contetn-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 10189

def test_status_code(): 
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Huskar' 


