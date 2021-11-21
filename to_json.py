import json

ar = []

with open('fuck.txt', encoding='utf-8') as f:
    for i in f:
        n = i.lower().split('\n')[0]
        if n != '':
                ar.append(n)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar,e)