# 載入Pandas
# import pandas as pd
# 列表資料為底,建立Series
# pd.Series(列表)
# data = pd.Series(料表)
# data.max() 資料最大數
# data.median() 資料中位數
# data.head()  印出資料前幾筆
# data.discribe() 觀察資料 摘要
# data = data*2 資料放大兩倍
# ------------------------------------------
# DataFrame
# 列表資料為底,建立DataFrame
# pd.DataFrame(字典)
# data["欄位名稱"]   直向可以取得指定欄位
# data.iloc[列編號]  橫向編號列 由橫向0開始
#                       axis=1直欄下
#               索引    name    Salary
# axis=0橫列      0      Amy     30000
#                1      John     50000
#                2      Bob      40000

# ------------------------------------------

# Series
import pandas as pd
# data = pd.Series([20, 10, 15])
# print(data)
# print('最大數', data.max())
# print('中位數', data.median())
# data = data*2
# print(data)
# # 比較運算
# data = data == 20
# print(data)

# ------------------------------------------
# DataFrame
# data = pd.DataFrame({
#     'name': ['Amy', 'John', 'Bob'],
#     'Salary': [30000, 50000, 40000]
# })
# print(data)
# print(data["name"])
# print(data.iloc[0])  # 印出第一 '列'
