import pandas as pd
# 篩選條件 (會與資料數量相對的布林值)
# Series
# 方法一Series  data = pd.Series(資料列表)
# condition = [True, False, True]  # 篩選條件True代表要的資料 False代表不要的資料
# filteredData = data[condition]  # 根據條件放進變數 完成篩選

# 方法二(常用)Series  data = pd.Series(資料列表)
# condition = data>5  # 篩選條件True代表要的資料 False代表不要的資料
# filteredData = data[condition]  # 根據條件放進變數 完成篩選

# DataFrame
# 資料清理
# data.dropna(axis=0) 移除 橫列 有空值的資料
# data.drop_duplicates() 移除 重複值

# 方法一 DataFrame  data = pd.DataFrame(字典)
# condition = [True, False, True]  # 欄位 篩選條件True代表要的資料 False代表不要的資料
# filteredData = data[condition]  # 根據條件放進變數 完成篩選

# 方法二(常用)DataFrame  data = pd.DataFrame(字典)
# condition = data[欄位名稱]>5  # 篩選條件True代表要的資料 False代表不要的資料
# filteredData = data[condition]  # 根據條件放進變數 完成篩選

# Series 篩選
# 數字
# data = pd.Series([30, 15, 20])
# condition = data > 18
# print(condition)
# newData = data[condition]
# print(newData)

# 字串
# data = pd.Series(['您好', 'Pandas', 'Python'])
# condition = data.str.contains('P')
# print(condition)
# filteredData = data[condition]
# print(filteredData)


# DataFrame 篩選
data = pd.DataFrame({
    'name': ['Amy', 'Bob', 'Charles'],
    'salary': [30000, 50000, 40000],
})
print(data)
print('-'*30)
# condition = data['salary'] >= 40000
# print(condition)
# print('-'*30)
# filterData = data[condition]
# print(filterData)
condition = data['name'] == 'Amy'
print(condition)
print('-'*30)
filterData = data[condition]
print(filterData)
