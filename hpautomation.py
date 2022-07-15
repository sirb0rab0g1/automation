from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

def main():
    # Set up Facebook login account name and password
    account = "superadmin@admin.com"
    password = "admin12"

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options, executable_path='./chromedriver')

    # login procedure
    driver.get('https://hpstaging.poolreno.com/')
    emailelement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/input')
    emailelement.send_keys(account)
    passelement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[3]/div/div[1]/div[2]/input')
    passelement.send_keys(password)
    time.sleep(1)
    loginelement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/button/div').click()
    time.sleep(2)
    # mag insert mog data didto sa sample.json


    # sample searching
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/aside/div[1]/div/div[2]/a/div[1]/i').click()
    time.sleep(2)
    searchelement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/main/div/main/div/div[1]/div/div/div/div/div/div[1]/input')
    searchelement.send_keys("adsfasdfasdf")
    searchelement.send_keys(" ")
    time.sleep(2)

    #logout
    driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/aside/div[2]/div/div/div/a').click()

    # Close driver
    time.sleep(100)
    # driver.close()

if __name__ == '__main__':
  main()
