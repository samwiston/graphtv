import json

data = {}

with open("basics.json", "r", encoding="utf8") as inFile:
    data = json.load(inFile)

print(data["tt0087305"])