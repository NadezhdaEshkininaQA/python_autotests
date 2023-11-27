import requests


responce = requests.post(url='https://api.pokemonbattle.me:9104/pokemons',
                         json={
                             
                            "name": "Бульбазавр",
                            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                        
                         },
                         headers={"trainer_token": "099e375fbd583f7b82fb79f0df6c56f7",
                                  'Content-Type':'application/json'}
                         
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')



responce = requests.put(url='https://api.pokemonbattle.me:9104/pokemons',
                         json={
                            "pokemon_id": 20444,
                            "name": "Бульбазавриха",
                            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                        
                         },
                         headers={"trainer_token": "099e375fbd583f7b82fb79f0df6c56f7",
                                  'Content-Type':'application/json'}
                         
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')


responce = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball',
                         json={
                            "pokemon_id": "20444"
                         },
                         headers={"trainer_token": "099e375fbd583f7b82fb79f0df6c56f7",
                                  'Content-Type':'application/json'}
                         
                         )
print (f'Code: {responce.status_code} - {responce.reason}. Message: {responce.text}')