from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()
# 隐式等待10秒
wd.implicitly_wait(10)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://cdn2.byhy.net/files/selenium/test3.html')
element=wd.find_element_by_id("input1")
element.clear()
element.send_keys('拜月黑羽')
wd.quit()