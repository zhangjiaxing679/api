import time
from selenium import webdriver

def loginAndCheck(username,password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('http://127.0.0.1/mgr/sign.html')
    if username is not None:
        driver.find_element_by_id('username').send_keys('byh')
    if password is not None:
        driver.find_element_by_id('password').send_keys('88888888')
    driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(2)

    alertText = driver.switch_to.alert.text
    print(alertText)
    driver.quit()
    return alertText
