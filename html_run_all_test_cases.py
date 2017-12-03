import os
import smtplib
import unittest
#htmltestrunner 是基于unittest框架的一个扩展，可以在网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner



def send_mail(path):
    #二进制的方式是加上b，rb是二进制的方法读
    f = open(path, 'rb')
    #f.read()
    #mail_body邮件正文
    mail_body = f.read()  #读取html报告的内容，作为邮件正文
    f.close()

    #要想发邮件，要把二进制内容转成MIME格式
    #MIME multipurpose多用途 internet mail extensions扩展
    #这种格式是对邮件协议的一个扩展，使邮件不仅支持文本，还支持多种格式,比如音频、图片，二进制文件等
    #msg
    msg = MIMEText(mail_body, 'html', 'utf-8')
    #上面是邮件正文，邮件除了正文，还有主题、发件人、收件人
    #msg是字典类型，类似于数组，区别是
    #1.字典是无序的:dicAndSet里有讲
    #dict = {}
    #student
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    #126邮箱先在邮箱里设置-授权码设置，自己写代码是客户端
    #如果想用客户端软件或者自己写代码登陆邮箱，很多类型的邮件，需要单独设置一个客户端授权码，为了邮箱安全着想
    #由于自己的邮箱没有设置授权码，所以发件箱统一用老师的邮箱账号
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = '13623828654@163.com'
    #msg['To'] = '742303846@qq.com'

    #现在邮件内容已经准备好了，下面开始发送邮件
    #发邮件的手动步骤：
    #1.打开登陆页面，即是连接邮箱服务器
    #要想连接服务器，首先要搞清楚网络传输协议
    # http,https,ftp,socket
    #发邮件的协议，一般有三种，你需要先查看邮箱支持哪种协议
    #126支持的三种协议是pop3,smtp,imap
    #选择一种协议，用来发邮件
    #smtp  simple mail transfer protocol简单邮件传输协议
    #首先导入smtplib的代码库
    smtp = smtplib.SMTP() #实例化一个SMTP类的对象
    smtp.connect("smtp.126.com") #连接126邮箱的服务器地址,一般是smtp.域名.com

    #2.登陆邮箱
    #smtp.login('bwftest126@126.com','abc123asd')
    smtp.login('bwftest126','abc123asd654')
    #3.发送邮件
    #sendmail ctrl键点击
    #smtp.sendmail(msg['From'], msg['To'], msg, mail_options=[],rcpt_options=[] )
    #msg是MIME类型，需要转换成string类型再发送
    #smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.sendmail('bwftest126@126.com', '13623828654@163.com', msg.as_string())
    #smtp.sendmail('bwftest126@126.com', 'huyinmei@atteam.cn', msg.as_string())

    #4.退出邮箱
    smtp.quit()
    print('email has sent out')


if __name__ == '__main__':
    #time要导包，str是String f是format格式
    #strftime()通过这个方法可以定义时间格式
    #为什么时间不用冒号：中划线可以作为文件名的一部分，冒号不能作为文件名的一部分
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
    #unittest.TextTestRunner()文本测试用例运行器
    #现在用htmltestrunner测试用例运行器
    #html的测试用例运行器最终会生成一个html格式的测试报告
    #我们是不是至少要指定测试报告的路径
    base_path = os.path.dirname(__file__)
    #path = base_path + "/report/report.html"
    #加入时间戳

    path = base_path + "/report/report" + now + ".html"
    file = open(path, 'wb')
    #HTMLTestRunner(stream=sys.stdout, verbosity=1, title=None,description=None).run(suite)
    #HTMLTestRunner(stream=file, title="海盗商城测试报告", description="测试环境：windows server2008 + Chrome").run(suite)
    HTMLTestRunner(file,1, "海盗商城测试报告", "测试环境：Windows server2008 + Chrome").run(suite)
    file.close()
    #要把html报告作为正文发送邮件
    #选中send_mail然后alt+enter选择create
    send_mail(path)
    #这时生成的测试报告，只显示类名和方法名，只能给专业人员kan
    #应该相关的手动测试用例的标题加到测试报告
    #自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写，我们就怎么编写代码，所以代码里应该可以体现手工测试用例的标题
    #新的测试报告会覆盖旧的，怎么保存所有的报告：
    #加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分可以避免文件名重复的问题：写在main下面
    #html的报告生成后，测试用例全部执行完成，可以生成一封提醒邮件，通知别人。
