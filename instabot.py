import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IE_DIR = os.path.join(BASE_DIR, 'geckodriver.exe')
AD_URL = 'https://www.instagram.com/'


class BOT():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=IE_DIR)

    def login_link(self):
        self.driver.get(AD_URL)
        sleep(1)
        # self.driver.find_element_by_xpath(
        # '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]').click()

    def login(self):
        user_id = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
        # user_id=self.driver.find_element_by_css_selector('div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        user_id.click()
        user_id.send_keys('monof62')
        user_pass = self.driver.find_element_by_css_selector(
            'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        user_pass.click()
        user_pass.send_keys('fa4420587490')

        btn = self.driver.find_element_by_css_selector(
            '.sqdOP > div:nth-child(1)')
        btn.click()
        sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(5)
        self.driver.find_element(
            By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    def like_photo(self, hashtag, amount):
        hashtag_url = 'https://www.instagram.com/explore/tags/'+hashtag
        self.driver.get(hashtag_url)
        sleep(5)
        self.driver.find_element_by_class_name('KC1QD').click()
        i = 1
        while i <= amount:
            sleep(5)
            btn_like = self.driver.find_element(
                By.XPATH, '/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            btn_like.click()
            sleep(3)
            self.driver.find_element_by_css_selector(
                '.fr66n > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').click()
            i += 1


if __name__ == '__main__':
    bt = BOT()
    bt.login_link()
    bt.login()
    bt.like_photo('python', 2)
