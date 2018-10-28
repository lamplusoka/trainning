#!/usr/bin/python3

import json #前回ファイルの読み込み
f = open("output.json", 'r')
json_data = json.load(f)
print("前回は" + json_data['日付'] + "に" + json_data['部位'] + "を鍛えました。" )

import sys
args = sys.argv #引数受け取り

if args[1] == "前側": #次回部位の特定
    json_data['部位'] = "下半身"
elif args[1] == "下半身":
    json_data['部位'] = "後側"
elif args[1] == "後側":
    json_data['部位'] = "前側"

import datetime
time = datetime.datetime.strptime(args[2], '%Y/%m/%d') #日付文字列をdatetimeへ変換
addtime = time + datetime.timedelta(days=1) #一日足す
nexttime = addtime.strftime('%Y/%m/%d') #日付を文字列へ変換

print("次回は"+ nexttime + "に" + json_data['部位'] + "をやりましょう。")

train = {'部位':args[1], '日付':args[2]} #今回の部位と日付をjsonファイルへ保存
f = open("output.json", "w")
json.dump(train, f, ensure_ascii=False)