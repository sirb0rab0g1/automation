from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

def main(groups, message):
    # Set up Facebook login account name and password
    account = "sdfadsfasf"
    password = "sdfadsfasf"

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
    driver.get('https://www.facebook.com')
    emailelement = driver.find_element(By.XPATH,'//*[@id="email"]')
    emailelement.send_keys(account)
    passelement = driver.find_element(By.XPATH,'//*[@id="pass"]')
    passelement.send_keys(password)
    time.sleep(1)
    loginelement = driver.find_element(By.XPATH,'//*[@name="login"]').click()
    time.sleep(2)

    # placeholder-arq94
    # Post on each group
    for group in groups:
        driver.get(group)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]').click() # to show modal yawa
        post_box = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div')
        # post_box[0].find_elements_by_class_name('dbpd2lw6 l9j0dhe7 stjgntxs ni8dbmo4 lzcic4wl idiwt2bm')
        # pasmo1 = post_box[0].find_elements_by_tag_name('form')
        # pasmo2 = pasmo1.find_element_by_class_name('dbpd2lw6 l9j0dhe7 stjgntxs ni8dbmo4 lzcic4wl idiwt2bm')

        # pasmo1 = post_box.find_elements_by_class_name('dbpd2lw6 l9j0dhe7 stjgntxs ni8dbmo4 lzcic4wl idiwt2bm')
        # pasmo2 = pasmo1.find_elements_by_class_name('kr520xx4 pedkr2u6 ms05siws pnx7fd3z b7h9ocf4 pmk7jnqg j9ispegn')
        #print(pasmo1)


        # post_box[0].find_element_by_class_name('fcg2cn6m pmk7jnqg cypi58rs')
        # print(post_box[0].size())
        for row in post_box:
            print(format(row.text))
            print(row.tag_name)
            print(row.get_attribute('innerHTML'))
            print(row.get_attribute('outerHTML'))
            pasmo = row.find_element(By.XPATH, "//*[contains(text(),'Create Post')]")
            driver.execute_script("arguments[0].innerText = '200'", pasmo)
            # print(row.find_element_by_class_name('83agx80 cbu4d94t lzcic4wl ni8dbmo4 stjgntxs oqq733wu l9j0dhe7 du4w35lb cwj9ozl2 ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi nwpbqux9'))
        #  row.find_element_by_class_name('.fcg2cn6m .pmk7jnqg .cypi58rs').click()
          # row.find_elements_by_xpath("//*[contains(text(), 'Create Post')]")
          # row.find_element_by_tag_name('span')
          #row.find_element(By.XPATH, '//*[@id="jsc_c_1f"]/span')
          # driver.find_element_by_name('username')
          #driver.execute_script('arguments[0].innerHTML = "New value";', row)
          #print(row)

    # Close driver
    time.sleep(100)
    # driver.close()

if __name__ == '__main__':
  groups = [
      "https://www.facebook.com/groups/468869437437684"
  ]
  message = "https://www.facebook.com/zxcasdqwe123qweasdzxc/posts/4247931625234505"
  main(groups, message)














  '''
        




        # print(str(post_box.is_displayed()))
        # post_box.click()
        # post_box.send_keys(message)
        # time.sleep(1)
        # # for photo in images_list:
        # #     photo_element = driver.find_element(By.XPATH,'//input[@type="file"]')
        # #     photo_element.send_keys(photo)
        # #     time.sleep(1)
        # time.sleep(6)
        # post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
        # clickable = False
        # while not clickable:
        #     cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
        #     if cursor == "pointer":
        #         clickable = True
        #     break
        # post_button.click()
        # time.sleep(5)'''
