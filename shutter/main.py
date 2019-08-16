import os
import sys
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui

dir_path = os.path.dirname(os.path.realpath(__file__))
print('当前工作路径:{}'.format(dir_path))
img_dir = os.path.join(dir_path,'images')
print("目标图片下载地址：{}".format(img_dir))


def INFO(message):
    SPACE = '.' * 22
    EMOJI = '📢 '
    if message is not '':
        print('Fuck Shutter INFO :\n')
        print(SPACE, EMOJI, message)
        print('\n')


def WARN(message):
    SPACE = '.' * 22
    EMOJI = '❗ '
    if message is not '':
        print('Fuck Shutter WARN :\n')
        print(SPACE, EMOJI, message)
        print('\n')


curDir = os.getcwd()
INFO(curDir)

URL = 'https://nohat.cc/tool/findstock'
# TEST_IMG = 'https://www.shutterstock.com/zh/image-illustration/ikat-seamless-pattern-design-fabric-523678297?studio=1'

with open("shutter.txt", "r") as ins:
    url_array = []
    for line in ins:
        url_array.append(line)

print('总共需要下载： {} 个图片'.format(len(url_array)))
print('准备下载....')
start_time = datetime.now()
print('开始工作时间: {}'.format(start_time))
count = 1
for each in url_array:
    print('准备下载....')
    INFO('正在设置默认下载地址...')
    chrome_options = Options()
    chrome_options.add_argument("download.default_directory={}".format(img_dir))
    INFO('正在使用Chrome作为默认浏览器')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    # driver = webdriver.Chrome()
    print('总共需要下载： {} 个图片'.format(len(url_array)))
    print('开始下载第 {} 个图片：'.format(count))
    URL = URL
    TEST_IMG = each
    INFO(URL)
    INFO(TEST_IMG)
    # chrome_options.add_argument('headless')
    INFO('正在打开下载地址')
    driver.get(URL)
    INFO('设置浏览器全屏显示')
    driver.maximize_window()
    INFO('正在查找输入框')
    driver.find_element_by_id('theurl').click()
    INFO('清除输入框中的已有元素')
    driver.find_element_by_id("theurl").clear()
    INFO('输入图片网址')
    driver.find_element_by_id("theurl").send_keys(TEST_IMG)
    INFO('等待搜索按钮')
    element_search = WebDriverWait(driver, 0.5, 60).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='trai']/div/div[2]/div/div/button"))
    )
    if element_search:
        element_search.click()
    INFO("等待 ‘Find Link' 按钮")
    element_find = WebDriverWait(driver, 1, 60).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(.,' Find Link')]"))
    )
    if element_find:
        element_find.click()
    INFO("开始 ’Click to View‘ 按钮")
    element_view = WebDriverWait(driver, 70).until(
        EC.element_to_be_clickable((By.ID, "taifile"))
    )   
    INFO('已经定位View')
    time.sleep(5)
    element_view.click() 
    print('View被点击了')
    print(element_view)
    time.sleep(5)
    try:
        element_view.click() 
    except:
        pass
    time.sleep(20)
    driver.close()
    INFO('即将删除已完成图片链接...')
    with open("shutter.txt", "r") as f:
        lines_of_shutter = f.readlines()
    with open("shutter.txt", "w") as f:
        for completed_line in lines_of_shutter:
            if completed_line.strip("\n") != TEST_IMG:
                f.write(completed_line)
    INFO('已下载图片地址成功删除...')    
    url_array.remove(each)
    count = count + 1
    time.sleep(60)

end_time = datetime.now()
print('结束工作时间:{}'.format(end_time))
print('总共下载了: {} 张图片，程序总用时：{} 秒'.format(len(url_array), (end_time - start_time).seconds))