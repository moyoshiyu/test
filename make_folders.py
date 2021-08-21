# GAMMASOFT 空フォルダを複数作成
# tenp.csv 内容
# 01,東京八重洲店
# 02,新橋店
# 03,御徒町店　
# https://gammasoft.jp/python-example/python-create-stores-folders-immediately/

import os
import csv

stores_path = 'tenpo.csv'
# stores_path = r"d:\\tenpo.csv"
# ファイルが共有フォルダにある場合
# stores_path = r'\\main-host\Shared Folders\Projects\tenpo.csv' 

with open(stores_path, encoding='cp932') as f:
    reader = csv.reader(f)
#    next(reader)    # ヘッダーを読み飛ばす場合付ける
    for row in reader:
        folder_name = row[0] + '_' + row[1]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)