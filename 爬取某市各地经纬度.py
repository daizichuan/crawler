# -- coding:UTF-8 --
import requests
import pprint
from lxml import etree
import csv

url = r'https://www.d1xz.net/xp/jingwei/guangdong.aspx'
headers = {
    "User-Agent":
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"
}
respose = requests.get(url, headers=headers)
HTML = etree.HTML(respose.text)
num = len(HTML.xpath('/html/body/div[4]/div[2]/div/div/table/tbody/tr'))
lst = []
for i in range(2, num + 1, 1):
    results = HTML.xpath(f'/html/body/div[4]/div[2]/div/div/table/tbody/tr[{i}]')
    tmp = []
    for j in range(3):
        tmp.append(results[0][j].text)
        # print(results[0][j].text)
    lst.append(tmp)

# # pprint.pprint(results)
headers = ['城市', '经度', '纬度']
with open('某市经纬度.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(lst)
