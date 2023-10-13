import json

lga_key = {}
with open('lga.json') as lga:
    data = json.load(lga)
    for g in data["objects"]["unnamed"]["geometries"]:
        
        try:
            lga_key[g["properties"]["ABB_NAME"]] += 1
        except:
            lga_key[g["properties"]["ABB_NAME"]] = 1

for k, v in lga_key.items():
    if v > 1:
        print(k, v)
