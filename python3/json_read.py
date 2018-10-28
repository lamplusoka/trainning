#!/usr/bin/python3
import json
f = open("output.json", 'r')
json_data = json.load(f)
print(json_data['部位'] + " " + json_data['日付'])