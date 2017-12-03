# 1.导入pymysql代码库
import pymysql

def connectDb():
    # 连接数据库，需要数据库的哪些信息
    # ip地址，端口号，用户名和密码，数据库名称……
    #要知道Connnect()需要那些参数，ctrl点击这个方法,再点击return Connection(*args, **kwargs)的Connection
    #pymysql.Connect(host=None, user=None, password="",
                 #database=None, port=0, unix_socket=None,
                 #charset='', sql_mode=None,
                # read_default_file=None, conv=None, use_unicode=None,
               # connect_timeout=10, ssl=None, read_default_group=None,
               #   compress=None, named_pipe=None, no_delay=None,
               #   autocommit=False, db=None, passwd=None, local_infile=False,
               #   max_allowed_packet=16*1024*1024, defer_connect=False,
               #   auth_plugin_map={}, read_timeout=None, write_timeout=None,
               #   bind_address=None)
    conn = pymysql.Connect(host="127.0.0.1", user="root", password="root",
                 database="pirate", port=3306,charset='utf8')
    #查询hd_user表中所有的数据，并且倒叙打印
    sql = "select * from hd_user order by id desc"
    #要想在代码中执行这条sql语句，首先要获得数据库的游标cursor
    curs = conn.cursor()
    #通过游标来执行sql语句
    curs.execute(sql)
    #要获取数据库中最新的记录
    #那么就要把数据库所有结果倒叙排列
    #然后用fetchone()方法获取第一条记录，即数据库中最新记录
    result = curs.fetchone()
    #如果想获取所有查询结果，fetchall()
    #result = curs.fetchall()
    return  result


#输入main按回车会出现下面这句
if __name__ == '__main__':
    print(connectDb())
