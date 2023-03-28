import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://katc.mil.kr/katc/community/children.jsp"
driver.get(url)

NAME = ""
DATE = ""
BIRTH = ""


driver.implicitly_wait(10)
date = Select(driver.find_element(By.CSS_SELECTOR, "#search_val1"))
# date.click()
date.select_by_value(DATE)
# date = driver.find_element(By.CSS_SELECTOR, "search_val1 > option:nth-child(6)")
birth = driver.find_element(By.CSS_SELECTOR, "#birthDay")
birth.send_keys(BIRTH)
name = driver.find_element(By.CSS_SELECTOR, "#search_val3")
name.send_keys(NAME)
name.send_keys(Keys.ENTER)

time.sleep(1)
driver.implicitly_wait(10)
selectAr = driver.find_element(By.CSS_SELECTOR, "#childInfo1")
selectAr.click()

driver.implicitly_wait(10)
writeStart = driver.find_element(By.CSS_SELECTOR, "#letterBtn")
writeStart.click()

driver.implicitly_wait(10)
humanCheck = driver.find_element(By.CSS_SELECTOR, "#fn_submit")
humanCheck.click()


driver.switch_to.window(driver.window_handles[-1])

driver.implicitly_wait(10)
checkAgenc = driver.find_element(By.CSS_SELECTOR, "#ct > fieldset > ul.agency_select__items > li:nth-child(2) > label").click()
confirm = driver.find_element(By.CSS_SELECTOR, "#ct > fieldset > ul.agreelist.all > li > span > label:nth-child(2)").click()
auth = driver.find_element(By.CSS_SELECTOR, "#btnSimple").click()

driver.implicitly_wait(10)
qrcode = driver.find_element(By.CSS_SELECTOR, "#btnQrTran").click()


# get authcode
driver.implicitly_wait(10)
authcode = driver.find_element(By.CSS_SELECTOR, "#qrCodeNum")

time.sleep(1)
code = authcode.get_attribute('value')

print(code)



time.sleep(5)
driver.close()
