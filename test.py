from selenium import webdriver
from selenium.webdriver.common.keys import Keys


go_to = input("where to? ").lower()

search = go_to.split("search for")[1]

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.google.com/")

search_box = driver.find_element_by_xpath(
    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_box.send_keys(search)
search_box.send_keys(Keys.ENTER)
