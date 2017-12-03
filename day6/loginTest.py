import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #现在这种测试用例可读性比较差，维护起来比较困难
        #那么测试用例写成什么样可读性比较好呢
        # 1.打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        #lp = LoginPage()    #实例化一个登陆页面,写一个loginPage.py
        lp = LoginPage(self.driver)
        lp.open()
        # 2.输入用户名
        #self.driver.find_element_by_id("username")
        #self.driver.find_element(By.ID, "username").send_keys("hymhym")
        lp.input_username("hymhym")
        # 3.输入密码
        #self.driver.find_element(By.ID, "password").send_keys("123456")
        lp.input_password("123456")
        # 4.点击登陆按钮
        #self.driver.find_element(By.CLASS_NAME, "login_btn").click()
        lp.click_login_button()
        # 5.验证是否跳转到管理中心页面
        #head里的title
        #expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        #浏览器里是否包含"我的会员中心"这几个字
        #运行下面这个会报错，因为登陆成功页面跳转后才是主页面，需要加时间等待
        #self.assertIn("我的会员中心", self.driver.title)
        #time.sleep(5)
        #self.assertIn("我的会员中心", self.driver.title)
        #pcp =   PersonalCenterPage()
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title, self.driver.title)



        #验证上面的测试用例是否全部都运行了，可以在最后写print方法
        #print("测试用例成功运行")
