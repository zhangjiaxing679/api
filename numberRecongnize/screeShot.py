import random
import time
import pytesseract
from selenium import webdriver
from PIL import Image

"""
    两种方式尝试
    1.截图识别数字
    2.selenium获取元素值 <div id="cTime">16:23:45:517</div>
"""
class number:
    def __int__(self,url):
        self.url=url

    def screeGetTime(self):
        '''
            1.截图获取数字
        '''
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(5)

        base_time = 60
        for i in range(10):
            random_time = random.randint(1, 60)
            time.sleep(base_time + random_time)
            driver.save_screenshot(F"../data/cTime0/time{i+1}.png")

        driver.close()
        for i in range(10):
            picture = Image.open(F"../data/cTime0/time{i+1}.png")
            picture = picture.crop((380, 200, 1200, 350))
            path=F"../data/cTime/time{i+1}.png"
            picture.save(path)
            print(pytesseract.image_to_string(Image.open(path), lang='chi_sim+eng'))

        # 截取部分
        # 确定元素的位置和大小并截取屏幕快
        # cTime = driver.find_element_by_id('cTime')
        # picture = Image.open(F"../data/test1/time1.png")
        # # picture = picture.crop(( cTime.location['y'],cTime.location['x'],
        # #                          cTime.location['x'] + cTime.size['width'],
        # #                          cTime.location['y'] + cTime.size['height']))
        # picture = picture.crop((380,200,1200,350))
        # # picture.save(F"../data/test2/time2.png")

    def webGetTime(self):
        '''
            2.selenium获取元素值
        '''
        driver = webdriver.Chrome()
        driver.get(url)

        # 每分钟随机截取一张图,
        # 如果是两台电脑就设置定时任务，随机时间取消，固定一分钟获取一次数值？？？
        base_time=60
        for i in range(10):
            random_time=random.randint(1,60)
            time.sleep(base_time+random_time)
            cTime = driver.find_element_by_id('cTime').text
            # 输出获取到的时间
            print(cTime)
        driver.close()

if __name__ == '__main__':
    # 北京时间校准网址
    url = "https://www.sucaifox.com/time/"
    # number().webGetTime()
    number().screeGetTime()


