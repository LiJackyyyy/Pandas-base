import pandas as pd
# data = pd.Series(資料列表)
# pd.Series(資料列表) 預設自動建立0開始的索引
# pd.Series(資料列表, index=索引列表) 自定義 索引必須和資料數量相同

# 觀察資料
# print(data.dtype) 印出資料型態
# print(data.size)  印出資料數量
# print(data.index) 印出索引的資料

# 取資料
# print(data[1]) 按照資料數字取值
# print(data[索引]) 利用索引取值

# 數字資料的運算 統計
# data = pd.Series([3, 10, 20, 5, -12])
# data.sum() 資料總和 , data.max() 資料最大數, data.prod()資料乘法總和
# data.mean() 資料平均, data.median()資料中位數, data.std() 標準差
# data.nlargest(3) 取前3大的數值, data.nsmallest(2) 取最小的2數

# 字串運算 都定義在 str 底層
# data = pd.Series(["您好", "Python", "Pandas"])
# data.str.lower()字串轉小寫, data.str.upper() 字串轉大寫, data.str.len() 字串長度
# data.str.cat(sep=",")把所有字串串連中間用,串再一起 , data.str.contains("P") 判斷字串中是否包含P字的
# data.str.replace("您好", "Hello") 將括弧的第一個參數由第二個參數取替

# datas = pd.Series([5, 4, -2, 3, 7, None],
#                  index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(datas)
# data = datas.dropna(axis=0)
# print(data)
# 觀察資料型態
# print("資料型態", datas.dtype)
# print("資料數量", datas.size)
# print("資料索引", datas.index)

# 取得資料
# print('根據順序編號', data[2], data[0])
# print('根據索引', data['e'], data['d'])


# 數字運算
# data = pd.Series([5, 4, -2, 3, 7],
#                  index=['a', 'b', 'c', 'd', 'e'])
# print('最大值', data.max())
# print('總和', data.sum())
# print('標準差', data.std())
# print('中位數', data.median())
# print('最大的三個數', data.nlargest(3))
# print('最小兩數', data.nsmallest(2))

# 字串運算
# data = pd.Series(['您好', 'Pandas', 'Python'])
# print('轉小寫',data.str.lower())
# print('字串長度', data.str.len())
# print('把字串串接的符號', data.str.cat(sep=','))
# print('判斷字串裡 <是否> 有P的字', data.str.contains('P'))
# print('取代', data.str.replace('您好', 'Hello'))