import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

lastURL = ""

with open("navercafe.conf", "r") as f :
    lastURL = f.readline().strip()



def returnLike() :
    like = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.ArticleContentBox > div.article_container > div.ReplyBox > div.box_left > div > div > a > em.u_cnt._count")
    return int(like.text)


# driver = webdriver.Chrome("/home/csk/Desktop/SeleniumTicketingMacro/chromedriver")
driver = webdriver.Chrome()
# driver.maximize_window()
driver.set_window_size(1620, 1020)
driver.get("https://cafe.naver.com/steamindiegame")


# 로그인창 접속
driver.implicitly_wait(10)
login = driver.find_element(By.CSS_SELECTOR, "#gnb_login_button > span.gnb_txt")
login.click()


# 로그인은 셀프로
input("로그인 후 아무거나 입력 : ")


# 마지막 게시물로 이동
driver.get(lastURL)
driver.implicitly_wait(10)
driver.switch_to.frame("cafe_main")
pageup = driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.ArticleTopBtns > div.right_area > a.BaseButton.btn_prev.BaseButton--skinGray.size_default > span")
pageup.click()


# 좋아요수 체크
driver.implicitly_wait(10)
time.sleep(3)



while True :
    try :
        like = returnLike() 
        while like != 0 :
            like = returnLike()
        #SE-bad6124a-2c6f-4cff-90f7-0ab9ec027e70 > div > div > div > a

        
    except NotImplementedError :
        input("Done?\t\t[YES|NO] : ")
        driver.close()