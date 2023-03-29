import time
import discohook
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://katc.mil.kr/katc/community/children.jsp"
driver.get(url)

NAME = "" # 이름 (한글)
DATE = "" # 입영일자 (YYYYMMDD)
BIRTH = "" # 생년월일 (YYMMDD)
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1090206620232974409/AUNHenHEge11oNIWOd5DBSh-GnhhJp9yW47RHJjiqvU7g1FcbuY21VblW2YngQwbqoyk" # 디스코드 웹훅 URL


driver.implicitly_wait(20)
date = Select(driver.find_element(By.CSS_SELECTOR, "#search_val1"))
date.select_by_value(DATE)
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


# PASS 인증코드 받기
driver.implicitly_wait(10)
authcode = driver.find_element(By.CSS_SELECTOR, "#qrCodeNum")

time.sleep(1)
code = authcode.get_attribute('value')

print(code)
discohook.sendwebhook(DISCORD_WEBHOOK_URL, code)

# while True :
#     remainTime = driver.find_element(By.CSS_SELECTOR, "#timeArea")
#     remainTime = remainTime.text
#     if remainTime


WebDriverWait(driver, 300).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

input("Sleeping...")
time.sleep(5)
driver.close()