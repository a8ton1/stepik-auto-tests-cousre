from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math
import time 


link = "http://suninjuly.github.io/selects2.html"

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver\chromedriver.exe')

    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = str(int(x) + int(y))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(z)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла