# -- coding:UTF-8 --
import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_column', 1000)

html = pd.read_html('xxx')
html[0].iloc[2:3214, 1:3].to_csv('1.csv', mode='w', encoding='utf_8', header=None, index=None)
# print(html)
