#coding:utf-8

import csv   #csvモジュールをインポートする
import json  #jsonモジュールをインポートする



#CSVファイルを開く
f = open('test.csv', 'rb')
dataReader = csv.reader(f)

for row in dataReader:
  if(row[0]==0):
      print('1line')
  else:
      print row

#http://d.hatena.ne.jp/fgshun/20100226/1267150983

#データを読み込む
#ヘッダ情報を取得する
#レコード情報を取得する
#変数に格納する
#ユーザ名を元に出力先のファイルをオープンする
#データ書き込む
#ファイルクローズする

#終わり

#ファイル名を元に
#
