# -- coding:UTF-8 --

import msvcrt
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import keyboard

tv_name_re = re.compile(r'《(.*?)》')

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化
driver.get('http://www.baidu.com')
try:
    with open('test.txt', 'r', encoding='utf-8') as f:
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            if not tv_name_re.findall(line):
                line = f.readline()
                continue
            tv_names = tv_name_re.findall(line)
            print(tv_names)
            if tv_names:
                for tv_name in tv_names:
                    # print(tv_name)
                    Flag = True
                    while Flag:
                        if keyboard.is_pressed('a'):
                            element = driver.find_element(by=By.ID, value='kw')
                            element.clear()
                            element.send_keys('韩剧 ' + tv_name)  # 输入搜索内容
                            element.send_keys(Keys.RETURN)  # 模拟回车
                            print('搜索!')
                            Flag = False
                        time.sleep(0.1)

            line = f.readline()
finally:
    driver.quit()
