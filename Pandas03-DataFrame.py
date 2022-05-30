import pandas as pd
# DataFrame 雙維資料(有欄有列)
# 以字典資料為底
# pd.DataFrame(字典) 預設自動建立0開始的索引
# pd.DataFrame(字典, index=索引列表) 自定義 索引必須和資料數量相同

# 觀察資料
# print(data.size)  印出資料數量 有幾個格子
# print(data.shape) 印出資料形狀 印出(列, 欄)
# print(data.index) 印出索引的資料
# print(data.columns) 印出資料欄位

# 取得 橫向列row 的資料
# print(data.iloc[1])   根據資料 順序編號 取<一整列>的值 (Series型態)
# print(data.loc[索引])  根據資料 索引 取<一整列>的值 (Series型態)

# 取得 直向欄column 的資料
# print(data[欄位名稱]) 根據資料 欄位名稱 取<一整欄>的值 (Series型態)
# 建立新欄位
# data['新欄位名稱'] = 列表資料
# data['新欄位名稱'] = Series 型態資料

#資料索引 pd.DataFrame(字典, index=索引列表)
# data = pd.DataFrame({
#     'name': ['Amy', 'Bob', 'Charles'],
#     'salary': [30000, 50000, 40000],
#     }, index=['a', 'b', 'c'])
# print(data)
# print("-"*30)
# 觀察資料
# print('資料數量', data.size)
# print('資料形狀 ( 列, 欄)', data.shape)
# print('資料索引', data.index)


# 取得列(Row 橫向) 的Series資料
# print('按照 <編號順序> 取得第二列', data.iloc[1], sep='\n')
# print('==========')
# print('按照<索引>取得第 c 列', data.loc['c'], sep='\n')

# 取得欄(column 直向) 的Series資料
# print('取得 name 欄位', data['name'], sep='\n')
# names = data['name']  # 取單維度的 Series 資料
# print('把name 全部轉大寫', names.str.upper(), sep='\n')
# salaries = data['salary']
# print('薪水平均', salaries.mean())

# 建立新欄位
# data['新欄位名稱'] = 列表資料
# data['revenue'] = [500000, 400000, 300000]
#
# # data['新欄位名稱'] = Series 型態資料 需要比較正規寫法
# data['rank'] = pd.Series([3, 6, 1], index=['a', 'b', 'c'])
# # 根據現有的欄位 去產生新的欄位
# data['cp'] = data['revenue'] / data['salary']
# print(data)
