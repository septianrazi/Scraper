from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from secrets import pw
from selenium.webdriver.common.action_chains import ActionChains

from myParser import getDetailsFromWebElement

import csv


PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}

chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(PATH, chrome_options = chrome_options)

driver.get("https://www.facebook.com/")
print(driver.title)

class FBBot:
    def __init__(self, driver, username, pw):
        super().__init__()
        self.driver = driver
        self.username = username
        self.pw = pw

    # initiates a login on Facebook given the credentials
    def login(self):
        email_field = self.driver.find_element_by_id("email").send_keys(self.username)
        pw_field = self.driver.find_element_by_id("pass").send_keys(self.pw)

        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()
        sleep(5)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']")))
        sleep(1)

    # tells driver to go to link
    def goTo(self, link):
        driver.get(link)

    # scrolls to the bottom of page
    def scrollDown(self):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(4)

    def scrollToBottom(self):
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            self.scrollDown()
            height = driver.execute_script("return document.body.scrollHeight")
            print (height)

    def getPosts(self):
        feed = self.driver.find_element_by_xpath("//div[@aria-label='News Feed']")
        post_list = feed.find_elements_by_xpath("//div[@role='article']")
        return post_list

    # function to click on all see mores
    def clickOnAllSeeMore(self):
        seeMoreButton = driver.find_elements_by_xpath("//a[@class='see_more_link']")
        for x in seeMoreButton:
            driver.execute_script("arguments[0].click();", x)

fbbot = FBBot(driver, "raziseptian@gmail.com", pw)
fbbot.login()
fbbot.goTo("https://www.facebook.com/groups/fennerhall")
# fbbot.goTo("https://www.facebook.com/groups/1611813365545792/")
fbbot.scrollToBottom()

fbbot.clickOnAllSeeMore()

post_list = fbbot.getPosts()

posts_data_list = []
for post in post_list:
    res = getDetailsFromWebElement(post)
    posts_data_list.append(res)
print(posts_data_list)

#convert to CSV
keys = posts_data_list[0].keys()
with open('data.csv', 'w', encoding="utf8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(posts_data_list)


print("///////////////////")
print("///////////////////")
print("///////////////////")

# print(post_list[0].page_source)
# print(post_list[3].page_source)


sleep(5)
print("done")
