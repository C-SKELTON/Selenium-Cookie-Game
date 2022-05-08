from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
chrome_driver_path = Service("C:/Users/conno/chrome_driver/chromedriver")

op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=chrome_driver_path, options=op)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

starting_time = 300
beg_time = 300
cookie = driver.find_element(By.ID, 'cookie')

#buyAlchemy\ lab > b

while beg_time >= 0:
    buy_cursor = driver.find_element(By.ID, 'buyCursor')
    buy_grandma = driver.find_element(By.ID, 'buyGrandma')
    buy_factory = driver.find_element(By.ID, 'buyFactory')
    buy_mine = driver.find_element(By.ID, 'buyMine')
    buy_shipment = driver.find_element(By.ID, 'buyShipment')
    buy_lab = driver.find_element(By.ID, 'buyAlchemy lab')
    buy_portal = driver.find_element(By.ID, 'buyPortal')
    buy_time_machine = driver.find_element(By.ID, 'buyTime machine')
    cursor_price = int(driver.find_element(By.CSS_SELECTOR, '#buyCursor > b').text.split("-")[1])
    grandma_price = int(driver.find_element(By.CSS_SELECTOR, '#buyGrandma > b').text.split("-")[1])
    factory_price = int(driver.find_element(By.CSS_SELECTOR, '#buyFactory > b').text.split("-")[1].replace(",",""))
    mine_price = int(driver.find_element(By.CSS_SELECTOR, '#buyMine > b').text.split("-")[1].replace(",",""))
    shipment_price = int(driver.find_element(By.CSS_SELECTOR, '#buyShipment > b').text.split("-")[1].replace(",",""))
    lab_price = int(driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab > b').text.split("-")[1].replace(",",""))
    portal_price = int(driver.find_element(By.CSS_SELECTOR, '#buyPortal > b').text.split("-")[1].replace(",",""))
    time_machine_price = int(driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine > b').text.split("-")[1].replace(",",""))
    money = driver.find_element(By.XPATH, '//*[@id="money"]')
    my_money = int(money.text.replace(",",""))
    if float(beg_time) <= starting_time - 5 + 5*.014 and float(beg_time) >= starting_time - 5 - 5*.014:
        if my_money >= time_machine_price:
            buy_time_machine.click()
        elif my_money >= portal_price:
            buy_portal.click()
        elif my_money >= lab_price:
            buy_lab.click()
        elif my_money >= shipment_price:
            buy_shipment.click()
        elif my_money >= mine_price:
            buy_mine.click()
        elif my_money >= factory_price:
            buy_factory.click()
        elif my_money >= grandma_price:
            buy_grandma.click()
        elif my_money >= cursor_price:
            buy_cursor.click()
        starting_time -=5
        #print(grandma_price)
    else:
        beg_time -= random.uniform(.001, .1)
        #print(beg_time)
        cookie.click()


driver.quit()
