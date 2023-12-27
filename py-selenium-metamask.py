from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def initChrome():
    global browser
    service = Service(executable_path='./chromedriver.exe')
    options = Options()
    options.add_argument(r"--user-data-dir=C:\Users\你自己的用户名\AppData\Local\Google\Chrome\User Data1")
    options.add_argument(r'--profile-directory=C:\Users\你自己的用户名\AppData\Local\Google\Chrome\User Data1\Profile 10')
    options.add_experimental_option('detach', True)  # 不自动关闭浏览器
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-address=127.0.0.1')
    options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(service=service, options=options)

def open_metamask():
    global browser
    browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
    time.sleep(2)
    browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('123456789') #解锁metamask
    browser.find_element(By.CLASS_NAME,'button').click()
    time.sleep(2)

def import_key(private_key):
    global browser,i
    ActionChains(browser).move_to_element(browser.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/button/span[1]/span')).click().perform()
    try:
        ActionChains(browser).move_to_element(
            browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div[4]/button')).click().perform()
    except:
        ActionChains(browser).move_to_element(
            browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div[3]/button')).click().perform()

    browser.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div[2]/div[2]/button').click()
    browser.find_element(By.XPATH,'//*[@id="private-key-box"]').send_keys(private_key)
    browser.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div[2]/div/div[2]/button[2]').click()
    time.sleep(2)

if __name__ == '__main__':
    browser=''
    try:
        initChrome()
        open_metamask()
    except:
        pass

    with open('./keys.txt', 'r') as f:
        keys = f.read().splitlines()
        i = 0
        for key in keys:
            try:
                i = i + 1
                print(key)
                import_key(key)
            except:
                browser.refresh()
                time.sleep(2)