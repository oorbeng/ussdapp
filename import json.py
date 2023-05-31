import json

with open("nominees.json", "r") as f:
    data = json.load(f)
    codes = data.keys()


variable = data["MS"]["Nominees"]




print(variable)
