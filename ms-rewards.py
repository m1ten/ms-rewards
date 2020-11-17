# WORKS BUT MAX 50 POINTS PER DAY.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

pause = 2

edge = webdriver.Edge("./msedgedriver.exe")
edge.get("https://bing.com/")

sleep(3)

# Signin
edge.find_element_by_id("id_s").click()

sleep(pause)

# Email
edge.find_element_by_id("i0116").send_keys("your_email")

sleep(pause)

# Next
edge.find_element_by_id("idSIButton9").click()

sleep(pause)

# Password
edge.find_element_by_id("i0118").send_keys("your_password")

sleep(pause)

# Signin
edge.find_element_by_id("idSIButton9").click()

sleep(pause)

# Stay signed in? yes.
edge.find_element_by_id("idSIButton9").click()

sleep(pause)

# Search

file = open('./words.json', 'r')
words = json.load(file)
file.close()

for word in words:
    edge.get("https://bing.com/")
    edge.find_element_by_id("sb_form_q").send_keys(word)
    edge.find_element_by_id("sb_form_q").send_keys(Keys.ENTER)
    sleep(pause)

sleep(15)
edge.close()

print("Complete!")
