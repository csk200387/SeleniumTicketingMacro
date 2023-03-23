# lms 출석 매크로

import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = ''
driver.get(url)
time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, "#header > div.utillmenu > ul")
login.click()
driver.implicitly_wait(10)
input_id  = driver.find_element(By.CSS_SELECTOR, "#usr_id")
input_id.send_keys(userID)
input_passwd = driver.find_element(By.CSS_SELECTOR, "#usr_pwd")
input_passwd.send_keys(userPasswd)
login = driver.find_element(By.CSS_SELECTOR, "#login_btn")
login.click()
print("login success")
driver.implicitly_wait(10)

join = driver.find_element(By.CSS_SELECTOR, "#contentsIndex > div.index-leftarea02 > div:nth-child(2) > ol > li:nth-child(9) > em")
join.click()
driver.implicitly_wait(10)
check = driver.find_element(By.CSS_SELECTOR, "#menu_attend")
check.click()
driver.implicitly_wait(5)

try :
    inp = driver.find_element(By.CSS_SELECTOR, "#pin")
    input_id.send_keys(input("출석번호 입력 : "))
    print("출석 성공")
except :
    print("출석시간이 아닙니다")
driver.close()
