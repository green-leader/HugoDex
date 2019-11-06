import json


def rowlookup(jsonlist, key, value):
    for row in jsonlist:
        typing = int
        if isinstance(value, str):
            typing = str
        if typing(row[key]) == typing(value):
            return row
    return None


def jsonJoin(json1, key1, json2, key2):
    '''Join two json documents along json1(key1), json2(key2)'''
    newjson = list()

    for item1 in json1:
        temp = rowlookup(json2, key2, item1[key1]).copy()
        if temp is not None:
            item1.update(temp)
            newjson.append(item1)
    return newjson


with open('json/types.json', 'r') as f:
    types = json.load(f)

with open('json/pokemon_types.json', 'r') as f:
    poke_types = json.load(f)

with open('json/pokemon.json', 'r') as f:
    poke = json.load(f)

newjson = jsonJoin(poke_types, 'type_id', types, 'id')

for x in newjson:
    print(x)
    break
for x in poke:
    print(x)
    break
