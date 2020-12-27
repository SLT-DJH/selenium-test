from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

def copy_input(driver, xpath, input) :
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

def goSuntable() :
    driver = webdriver.Chrome()
    url = 'https://google.com'

    driver.get(url)

    driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('썬 테이블')
    driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('.LC20lb.DKV0Md').click()

    driver.find_element_by_xpath("//div[@class='nav sub-menu sub_menu_hide  v-menu-type1 menu-vertical row-cnt-3 row-cnt-mobile-3']/ul/li[@data-code='m202004152c81c6f5f4a24']/a").send_keys(Keys.ENTER)

    driver.quit()

def goKkamdung() :
    driver = webdriver.Chrome()
    url = 'https://www.naver.com'

    driver.get(url)
    time.sleep(1)

    copy_input(driver, "//input[@id='query']", "63빌딩 돌상")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@id='query']").send_keys(Keys.ENTER)
    time.sleep(1)

    driver.find_element_by_xpath("//a[@href='https://blog.naver.com/kongminsook66']").click()
    time.sleep(1)

    driver.quit()

for i in range(10) :
    goKkamdung()