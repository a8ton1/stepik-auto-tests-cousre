from selenium import webdriver

import math
import time 


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver\chromedriver.exe')

    browser.get(link)
    
    button_a = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла