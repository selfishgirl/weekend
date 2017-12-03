# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("hym")
#driver.find_element_by_id("username").send_keys(Keys.TAB)
#链表和数组不同，数据有固定的长度，链表必须要y有明确的结束标志
ActionChains(driver).send_keys(Keys.TAB).send_keys("1qaz!QAZ").send_keys(Keys.ENTER).perform()
#2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改个人信息
#clear 是清空的意思，用来清空元素中原本的内容
#更好的变成习惯，在每次执行sendkeys之前，都进行一遍clear操作
# 4a. 真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("米米")
# 4b. 性别
#driver.find_element_by_css_selector('[value="2"]').click()
#如果value有相同的，可以用id和value同时定位
# css可以用多个属性组合定位一个元素
# 一个元素的多个属性之前不能有空格（空格表示下一代）
driver.find_element_by_css_selector('#xb[value="2"]').click()
#js删除代码 console里document.getElementById("date")按enter建 <input type="text">清除后可以用下面这个代码
#driver.find_element_by_id("date").send_keys("1974-10-24")
#js是一个单独语言，和python的语法不一样，不能直接在pycharm中执行
# js='document.getElementById("date").removeAttribute("readonly")'
#driver.execute_script(js)
#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("1974-10-24")
#用arguments改写上面输入,用selenium的定位方式，定位元素后，对元素执行js脚本，删除readonly属性
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("1974-10-24")
#用selenium调用js，一共有两个关键字：
# 1. arguments[]:表示用python语言代替一部分js,有时selenium定位比较容易
# 2.return 把js的执行结果返回给python语言，有时selenium定位不到的元素，可以用js定位到

#driver.execute_script("return document.getElementById('date')")
#date = driver.execute_script("return document.getElementById('date')")
#上面这句话====driver.find_element_by_id("date")
#date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1570588255")
driver.find_element_by_class_name("btn4").click()
#出现一个alert弹框，右键检查不到html代码的alert弹框,有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的，所以implictly_wait对这个控件不起作用
#所以就算上面写了implictly_wait，这个time.sleep()方法不能省略
#切换到alert的方法，和切换窗口的方法类似
#alert弹框，accept接受或同意或确定，dismiss拒绝或取消
#不修改信息的情况下，运行会报修改信息失败；alert后面没有括号
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()
