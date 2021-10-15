from selenium import webdriver

import time
import os 


link = "http://suninjuly.github.io/file_input.html"

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver\chromedriver.exe')

    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".form-group > [name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".form-group > [name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".form-group > [name='email']")
    input3.send_keys("@@")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    button1 = browser.find_element_by_id("file")
    button1.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла