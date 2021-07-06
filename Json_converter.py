import json

with open('tube_01.json', "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)

print(json_data)
print(json_data["records"])

# Git 반영 여부를 확인하기 위한 주석 추가