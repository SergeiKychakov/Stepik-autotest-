link = "http://selenium1py.pythonanywhere.com/"

#parser.addoption('--browser_name', action='store', default="chrome",
#help="Choose browser: chrome or firefox")
def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
