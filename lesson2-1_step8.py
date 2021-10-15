from selenium import webdriver

import math
import time 


link = "http://suninjuly.github.io/get_attribute.html"

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver\chromedriver.exe')

    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element_by_id("treasure")
    x_checked = x_element.get_attribute("valuex")
    x = x_checked
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox").click()
    option2 = browser.find_element_by_id("robotsRule").click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла