#!/usr/bin/python3
import sys
args = sys.argv
import json
f = open("output.json", 'r')
json_data = json.load(f)
print("前回は" + json_data['日付'] + "に" + json_data['部位'] + "を鍛えました。" )
print(args[2])