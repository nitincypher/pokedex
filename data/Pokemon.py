def getPokemonNames():
    import requests
    import json

    r=requests.get('https://github.com/sindresorhus/pokemon/raw/master/data/en.json')
    json_str = r.json()
    return json_str