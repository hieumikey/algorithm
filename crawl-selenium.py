from collections import UserString
from selenium import webdriver
import time
import pandas as pd
import os
import urllib.request
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(executable_path="C:/Users/admin/Desktop/chromedriver.exe")
url = "http://45.79.43.178/source_carts/wordpress/wp-admin"
driver.get(url)
time.sleep(5)
driver.find_elements_by_id("user_login").send_keys("admin")
driver.find_elements_by_id("user_pass").send_keys("123456aA")
driver.find_element_by_id("wp-submit").click()
uname = driver.find_element_by_id("wp-admin-bar-my-account").text
print(uname)
