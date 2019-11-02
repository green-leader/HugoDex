import csv
import json
import os

for dirpath, dirnames, filenames in os.walk('./csv'):
    pass

if not os.path.exists('json'):
    os.mkdir('json')

# Convert csv to json

for f in filenames:
    with open('csv/' + f) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        pre, ext = os.path.splitext(f)
        with open('json/' + pre + '.json', 'w') as outfile:
            out = json.dumps([row for row in csv_reader])
            print(out, file=outfile)
