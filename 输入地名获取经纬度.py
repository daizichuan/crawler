# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# URL
url = r'https://jingweidu.bmcx.com/'

# header
ua = (
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"'
)

options = webdriver.ChromeOptions()
# 谷歌无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
# header
options.add_argument('user-agent=%s' % ua)
browser = webdriver.Chrome(chrome_options=options)

# 打开URL
browser.get(url)

result = []
for i in range(1):
    browser.implicitly_wait(2)
    # 点击生成MAC按钮
    browser.find_element(by=By.XPATH, value='//*[@id="fen_xi_di_qu"]').clear()
    browser.find_element(by=By.XPATH, value='//*[@id="fen_xi_di_qu"]').send_keys("成都市")
    browser.find_element(by=By.XPATH, value='//*[@id="api_map_top"]/input[2]').click()
    browser.implicitly_wait(2)
    # 获取生成的MAC文本
    time.sleep(1)
    longitude = browser.find_element(by=By.XPATH, value='//*[@id="all_lng_show"]').get_attribute('value')
    latitude = browser.find_element(by=By.XPATH, value='//*[@id="all_lat_show"]').get_attribute('value')
    result.append(float(longitude))
    result.append(float(latitude))
print(result)

# 把结果放到csv里
# test = pd.DataFrame(columns=["mac"], data=result)
# test.to_csv('d:/mac.csv', encoding='utf-8', index=None)

# 退出浏览器
browser.quit()
