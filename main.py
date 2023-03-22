import time
import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By

# 사이트 로그인 정보
userId = ""
userPasswd = ""



driver = webdriver.Chrome()
driver.set_window_size(1620, 1020)
# driver.maximize_window()

# 사이트 주소
url = "https://www.playkfa.com/"
driver.get(url)
driver.implicitly_wait(10) # 셀레니움 암묵적 대기

# 로그인 시도
login = driver.find_element(By.CSS_SELECTOR, "body > div > div.header > div.header-top > div > ul > li.loginMenu > a")
login.click()

driver.implicitly_wait(10)

# id, passwd 입력 후 로그인
input_id  = driver.find_element(By.CSS_SELECTOR, "#loginID")
input_id.send_keys(userId)
input_passwd = driver.find_element(By.CSS_SELECTOR, "#loginPW")
input_passwd.send_keys(userPasswd)
login = driver.find_element(By.CSS_SELECTOR, "#form_login > button")
login.click()
print("login success")
time.sleep(2)

# 예매창 접근
driver.get("https://shop.playkfa.com/ticket/mennationalteam")
print("hear?")
driver.implicitly_wait(10)
yeme = driver.find_element(By.CSS_SELECTOR, "body > div > div.content.sub.ticket > div.content-section > div.ticket-content > div.tabs > div:nth-child(2) > div > ul > li:nth-child(1) > div.action > div.btn-reservation_wr > button")
yeme.click()
time.sleep(2)

# 팝업창이 뜰 경우 해당 창으로 전환
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)


try :
    while True :
        # 팝업 창의 좌석현황이 iframe 내에서 진행되어 frame 으로 전환
        driver.switch_to.frame('ifrmSeat')
        for tmp in range(4) :
            # 좌석의 상태를 불러옴
            thirdSitName = driver.find_element(By.CSS_SELECTOR, f"body > div > div.bodyZone > div.groundList > div.list > a:nth-child({tmp+24}) > span:nth-child(1)")
            thirdSitStatus = driver.find_element(By.CSS_SELECTOR, f"body > div > div.bodyZone > div.groundList > div.list > a:nth-child({tmp+24}) > span:nth-child(2)")
            print(thirdSitName.text, thirdSitStatus.text)
        print("="*50)
        time.sleep(5)
        driver.refresh() # 5초마다 새로고침

except Exception as e:
    print(e)
    driver.close() # 에러 발생시 종료
    exit()
