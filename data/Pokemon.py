def getPokemonNames():
    import requests
    import json

    r=requests.get('https://github.com/nitincypher/pokedex/raw/master/data/poke_data.json')
    json_str = r.json()
    return json_str