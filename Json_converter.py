import json

with open('tube_01.json', "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)

print(json_data)
print(json_data["records"])