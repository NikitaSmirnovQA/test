import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6ca1289e4839f842e1117f3e78717d60'
HEADER = {'Contetn-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
      "trainer_token": TOKEN,
    "email": "nikitaismirnov95@yandex.ru",
    "password": "9502020aA!"
}
body_pokemons = {
    "name": "Huskar",
    "photo_id": 3
}
body_putpokemons = {
    "pokemon_id": "70731",
    "name": "Puk",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "70731"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''     

'''response_pokemons = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response_pokemons.text)'''

'''response_pokemons = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_putpokemons)
print(response_pokemons.json)'''

response_pokemons = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokemons.json)