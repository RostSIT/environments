from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_site_contains_add_to_basket_button(browser):
    global button
    browser.get(link)
    browser.execute_script('return arguments[0].scrollIntoView(true)',
                           browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button'))
    button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')


def test():
    assert len(button) > 0, 'No Such basket Element'
