from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')
time.sleep(2)
searchBox = driver.find_element_by_name('search_query')
submit = driver.find_element_by_id('search-icon-legacy')
searchBox.send_keys('Hello world but its a Python youtube automation')
submit.click()
