from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = r'D:\chrome\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
sleep(2)
username.send_keys('your_user_name')
password = webdriver.find_element_by_name('password')
sleep(3)
password.send_keys('your_password')


button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(6)

webdriver.get('https://www.instagram.com/developer_md_92/')

sleep(4)
webdriver.find_element_by_class_name('_81NM2').click()
sleep(3)#//*[@id="react-root"]/section/main/div/ul/li[3]/a

for x in range(1,500):
    try:
        if webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[3]/button').text == 'Following':
            webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[3]/button').click()
            sleep(2)
            webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            sleep(7)
        webdriver.find_element_by_link_text('Next').click()
    except:
        continue
