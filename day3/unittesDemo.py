#测试框架是干什么用的
#主要是组织和执行测试用例
#1.导入unittest框架
import  unittest

#java中类名和文件名的关系，public类名和文件名一样
#python中的可以一样，推荐文件名首字母小写，类名首字母大写，其余一样
#2.继承unittest中的父类
#python中的继承直接用小括号表示
#TestCase是测试用例的意思，我们在UnittestDemo中编写测试用例
class UnittestDemo(unittest.TestCase):
    #3.重写父类中的方法setUp和tearDown
    #def是方法的关键字
    #setUp创建
    #类似于手动测试中的预置条件
    def setUp(self):
        print("这个方法将会在测试用例执行之前执行")
    def tearDown(self):
         print("这个方法将会在测试用例执行后执行")
#4.编写测试用例方法
    #只有以test开头命名的方法才是测试用例方法
    #测试用例方法可以直接运行，
    # 普通方法不能直接运行，只有被调用，才会执行
    #下面这几个方法，光标定位不一样，执行的结果不一样
    def test_log_in(self):
        print("登陆测试用例")
        self.zhu_ce()
    def zhu_ce(self):
        print("注册测试用例")
    #def test_log_out(self):
       # print("登出测试用例")
    def test_search(self):
        print("搜索测试用例")
#如果直接执行这个文件，那么就会执行下面的语句
#否则，执行其他文件，import这个文件的时候，下面的代码不会被执行
if __name__=='__main__':
    #执行当前文件中所有的unittest的测试用例；光标在main()后执行所有
    unittest.main()
    #python中实例化和java一样
    #UnittestDemo().zhu_ce()

