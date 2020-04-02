import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Open Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
# options.add_argument("--disable-notification")
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(r'C:\Users\Faris Hussain\Desktop\chromedriver', chrome_options=chrome_options)
driver.get("https://www.facebook.com/")


# driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']").send_keys("Hello this is automated Post")

# while True:
#     try:
#         post_btn = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
#         post_btn.click()
#         break
#     except NoSuchElementException:   


# driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']").send_keys("Hello this is automated Post")

# while True:
#     try:
#         post_btn = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
#         post_btn.click()
#         break
#     except NoSuchElementException:   

# driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']").send_keys("Hello this is automated Post")

# while True:
#     try:
#         post_btn = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
#         post_btn.click()
#         break
#     except NoSuchElementException:   



#Search for Email and Password Field and enter.

driver.find_element_by_id("email").send_keys("moh_lia@hotmail.com")
driver.find_element_by_id("pass").send_keys("Allah_or_Rasol1")
driver.find_element_by_id("loginbutton").click()
print(driver.title)

# ((By.XPATH, "//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']"))
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']")))
driver.get("https://www.facebook.com/permalink.php?story_fbid=3133479626790949&id=100003868288862")

# ((By.PATH, "//div[starts-with(@id, 'u_0_11')]//div[@class='_4299']//div[@class='_3w53']//div[@class=' _65td']"))

count = 0
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'u_0_')]//div[@class='_7c-t']"))).click()

while True:
    time.sleep(5)
    try:
        count = 0
        while (count <100):
            count = count + 1
            driver.find_element_by_xpath("//div[starts-with(@class, '_1p1t')]")
            comment = driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//div[@class='notranslate _5rpu']").send_keys("Haye Haye", Keys.ENTER)
            print(count)
        # count = 0
        # while (count <100):
        #     count = count + 1
        #     driver.find_element_by_xpath("//div[starts-with(@class, '_1p1t')]")
        #     comment = driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//div[@class='notranslate _5rpu']").send_keys("Nhi Dia Acha?", Keys.ENTER)
        break
    except NoSuchElementException:
        pass
#For Post

# driver.find_element_by_xpath("//div[starts-with(@id, 'u_0_')]//textarea[@name='xhpc_message']").send_keys("Hello this is automated Post")

# while True:
#     try:
#         post_btn = driver.find_element_by_xpath("//button[@class='_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")
#         post_btn.click()
#         break
#     except NoSuchElementException:    