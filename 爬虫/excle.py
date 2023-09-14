
import pandas as pd

# 读取文本文件
data = pd.read_csv('弹幕.txt', delimiter='\t')

# 将数据保存为Excel文件
data.to_excel('弹幕1.xlsx', index=False)