import unittest

import time
from selenium import webdriver


class MemberMangeTest(unittest.TestCase):
    #变量前加上self,表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        #打开浏览器
        #driver声明在setUp方法内是局部变量，不能被其他方法访问，tearDown访问时报错
        #webdriver  alt+enter导入包
        #driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器升级的话，下面这句话可以注释掉
        self.driver.maximize_window()

    def tearDown(self):
        #quit()退出整个浏览器
        #close()关闭一个浏览器
        #代码编写和调试的时候需要在quit()方法前加一个时间等待，方便看清楚执行过程
        #正式运行时去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        self.driver.quit()
    def test_add_member(self):
        # self.driver.get("网址")
        driver = self.driver
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_class_name("Btn").click()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.switch_to_frame("mainFrame")
        #driver.get("http://localhost/index.php?m=admin&c=index&a=index&pid=4#")
        driver.find_element_by_name("username").send_keys("cxy")
        driver.find_element_by_name("mobile_phone").send_keys("13623828654")
        driver.find_element_by_css_selector('[value="1"]').click()
        driver.find_element_by_id("birthday").send_keys("1982-11-24")
        driver.find_element_by_name("email").send_keys("13623828654@qq.com")
        driver.find_element_by_name("qq").send_keys("1570588246")
        driver.find_element_by_class_name("button_search").click()
s

