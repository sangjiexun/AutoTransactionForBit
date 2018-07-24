import csv
import pandas as pd
import numpy as np
from sklearn import preprocessing
#%matplotlib inline

#CSVファイルをListとして読み込む
#データ15件の最初と最後の取引価格の差額を算出
def input_csv():
	csv_file = open("C:/Users/nsait/AutoTransactionForBit/all_data.csv", "r", encoding="ms932", errors="", newline="" )
	#リスト形式
	data_list = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
	#データ15件ごとの価格変化を算出
	count = 0
	ltp_start = 0
	ltp_end = 0
	for row in data_list:
		if count == 0:
			ltp_start = float(row[1])
			count += 1
		elif count == 14:
			ltp_end = float(row[1])

			print(ltp_end - ltp_start)

			count = 0
		else:
			count += 1
		#print(row)

#CSVファイルをPandasで取得
def input_csv_byPandas():
	data_list = pd.read_csv('C:/Users/nsait/AutoTransactionForBit/all_data.csv', header=None)
	#取得したデータをグラフ描画
	#data_list.plot()
	#取得したデータを配列に変換
	#data_array = data_list.values
	#print(data_list[1])

	#データ15件ごとの価格変化を算出
	t = np.empty(3)
    #データ15件ごとの価格変化を算出
	count = 0
	ltp_start = 0
	ltp_end = 0
	for row in data_list.itertuples():
		if count == 0:
			#print(row[2])
			ltp_start = row[2]
			count += 1
		elif count == 14:
			#print(row[2])
			ltp_end = row[2]
			ltp_gap = ltp_end - ltp_start

			#なぜか全部[0, 0, 0]となる...。
			if ltp_gap >= 500:
				np.vstack((t, [1, 0, 0]))
			elif ltp_gap <= -500:
				np.vstack((t, [0, 1, 0]))
			else:
				np.vstack((t, [0, 0, 1]))
			count = 0
		else:
			count += 1
		print(t)

input_csv_byPandas()
