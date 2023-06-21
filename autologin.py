import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.chrome.options import Options
import subprocess
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chromeCookie"')
url = "https://goteacher.xyz"


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.maximize_window()
driver.get(url)
time.sleep(3)

#네이버 ID 비밀번호
user_id = 'j991132'
user_pw = '8888'

# 로그인창으로 접속
elem = driver.find_element(By.XPATH, '//*[@id="h6-info1"]/div[3]/ul/li[2]/a')
elem.click()

time.sleep(3)

#아이디 입력
log_ID = driver.find_element(By.ID, "login_id")
# log_ID.send_keys(user_id)
log_ID.click()
pyperclip.copy(user_id)
log_ID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#비밀번호 입력
log_PID = driver.find_element(By.ID, "login_pw")
log_PID.click()
pyperclip.copy(user_pw)
log_PID.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

#로그인 클릭

log_ENT = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div[3]/button')
log_ENT.click()
time.sleep(3)

#일간 클릭
daily = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/a[4]')
daily.click()
time.sleep(3)

#복무추가 클릭
bokmuadd = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div/div[4]/div[10]/a/div')
bokmuadd.click()
time.sleep(3)


#복무자 명
bo_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/section/form/div[2]/div[1]/div/input')
bo_name.send_keys("이름")