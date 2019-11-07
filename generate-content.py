import json
import os

dataPath = 'json/data/api/v2/'
outputPath = 'site/content/posts/'


def getPokemonCount():
    with open(dataPath + 'pokemon/index.json') as f:
        index = json.load(f)
    return index['count']


def genPokePages():
    for dirpath, dirnames, filenames in os.walk(dataPath + 'pokemon'):
        break
    for item in dirnames:
        indexPath = dataPath + 'pokemon/' + item + '/index.json'
        outPath = outputPath + item + '.md'
        with open(outPath, 'w') as out, open(indexPath, 'r') as f:
            data = json.load(f)
            data['title'] = data['name']
            json.dump(data, out)


if __name__ == '__main__':
    genPokePages()
