from time import sleep
from selenium import webdriver
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get("https://www.instagram.com/")
login_link = browser.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button')
login_link.click()
sleep(5)
browser.close()
