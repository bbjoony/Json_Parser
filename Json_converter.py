import json
import pandas as pd

with open('tube_01.json', "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
    df = pd.json_normalize(json_data["records"])
    df.to_csv('sample.csv')