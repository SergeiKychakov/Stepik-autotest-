import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By

        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_css_selector('[placeholder = "Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("S@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        from selenium import webdriver
        import time
        from selenium.webdriver.common.by import By
        
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_class_name('form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_class_name('form-control.second')
        input2.send_keys("Petrov")
        #input3 = browser.find_element_by_class_name('form-control.third')
        #input3.send_keys("S@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()