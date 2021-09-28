import pytest
from selenium import webdriver
import time
import math

global_text = ''
correct = "Correct!"

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', [("https://stepik.org/lesson/236895/step/1"), ("https://stepik.org/lesson/236896/step/1"), 
("https://stepik.org/lesson/236897/step/1"), 
("https://stepik.org/lesson/236898/step/1"), 
("https://stepik.org/lesson/236899/step/1"), 
("https://stepik.org/lesson/236903/step/1"), 
("https://stepik.org/lesson/236904/step/1"), 
("https://stepik.org/lesson/236905/step/1")])
def test_send_time(browser, url):
    link = f"{url}"
    browser.get(link)
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_xpath('//button[text()="Отправить"]')
    button.click()

    time.sleep(2)
    
    correct_element = browser.find_element_by_tag_name('pre')  
    correct_element1 = correct_element.text
    assert correct_element1 == correct, \
        print(correct_element1)

