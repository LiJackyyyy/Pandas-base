import pandas as pd
# 第一步  收集資料 (例如:爬蟲, 自動化收集資料)
# 第二步  資料清洗 (清理雜訊的資料)
# 第三部  分析資料

# 讀取資料
data = pd.read_csv('googleplaystore.csv')
# 觀察資料
print(data)
print('資料數量', data.size)
print('資料欄位', data.columns)
print('-'*30)

# 分析資料: 評分 統計數據
# print(data['Rating'])
# condition = data['Rating'] <= 5
# data = data[condition]
# print('平均數', data['Rating'].mean())
# print('中位數', data['Rating'].median())
# print('前一千筆的評分的平均數', data['Rating'].nlargest(1000).mean())

# 分析資料:安裝數量 統計數據
# to_numeric 把資料轉換成數字
# data['Installs'] = pd.to_numeric(data['Installs'].str.replace('[,+]', '', regex=True).replace('Free', '', regex=True))
# # print(data['Installs'][10472])
# # print(data['Installs'])
# print('平均數', data['Installs'].mean())
# condition = data['Installs'] > 100000
# print('安裝數量大於10萬', data[condition].shape[0])

# 基於資料的應用:關鍵字搜尋
# keyword = input('請輸入關鍵字:')
# # 應用程式裡面 是否包含輸入的關鍵字
# condition = data['App'].str.contains(keyword, case=False)  # case=False 忽略大小寫
# print('包含關鍵字的數量', data[condition]['App'].shape[0])

