import pandas as pd

# 準備資料
products = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava']
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

# 1. 使用字典方式建立 DataFrame
data_dict = {'Product': products, 'Price': prices, 'Sales': sales}
df_dict = pd.DataFrame(data_dict)

# 2. 使用列表(子列表)方式建立 DataFrame
data_list = [['Apple', 30, 100], ['Banana', 20, 150], ['Orange', 25, 80],
             ['Mango', 60, 60], ['Grape', 45, 90], ['Guava', 35, 54]]
df = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

# 觀察資料
print(df.head()) # 前5筆
print(df.tail()) # 後5筆
print(df.shape)  # 列數與欄數
print(df.columns)# 欄位名稱
print(df.dtypes) # 資料型態
print(df.count())# 非空值數量

# 計算統計資訊 (僅針對數值欄位)
stats = df.describe().round(2)
print(stats)

# 存檔
stats.to_csv('0520_stock2.csv')