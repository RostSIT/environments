from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_for_different_languages(browser):
    global button
    browser.get(link)
    button = browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button')


def test_site_contains_add_to_basket_button():
    assert len(button) > 0, 'No Such basket Element'
