#!/usr/bin/python3
import json
train = {
    '部位':'前側', '日付':'2018/10/28'
}
f = open("output.json", "w" )
json.dump(train, f, ensure_ascii=False)
