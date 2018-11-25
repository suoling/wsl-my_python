import requests
from bs4 import BeautifulSoup
import sqlite3
import os

baseUrl = "http://www.mm131.com/xinggan/"


def getImgParent(url):
    print('发送HTTP请求，并解析html，这是一个非常耗时的操作')
    res = requests.get(url)
    res.encoding = "gbk"
    soup = BeautifulSoup(res.text, "html.parser")
    dl = soup.find_all('dl', 'list-left public-box')
    return dl


def getImgSrc(dl):
    imgArr = dl[0].find_all('img')
    imgSrcArr = []
    for imgItem in imgArr:
        imgSrcArr.append(imgItem['src'])
    return imgSrcArr


def getNextPageUrl(dl):
    pageArr = dl[0].find_all('dd', 'page')[0].find_all('a')
    reqUrl = ''
    for pageItem in pageArr:
        if pageItem.get_text() == '下一页':
            reqUrl = baseUrl + pageItem['href']
    return reqUrl

def downLoadImg(imgArr):
    head = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'Accept-Encoding',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'img1.mm131.me',
        'Referer': 'http://www.mm131.com/xinggan/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    count = 0
    for imgArrItem in imgArr:
        for imgItem in imgArrItem:
            count += 1
            img = (count, imgItem)
            imgArrs.append(img)
            fp = open('C:\\Users\\yaoyuan\\PycharmProjects\\Demo\\images\\' + str(count) + '.jpg', 'wb')
            fp.write(requests.get(imgItem, headers=head).content)
            fp.close()

    init()


# ---------------------------------------------------------------------------------
# 将美女图片写入表中
# ---------------------------------------------------------------------------------


def get_conn(path):
    '''获取到数据库的连接对象，参数为数据库文件的绝对路径
    如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
    路径下的数据库文件的连接对象；否则，返回内存中的数据接
    连接对象'''
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')


def get_cursor(conn):
    '''该方法是获取数据库的游标对象，参数为数据库的连接对象
    如果数据库的连接对象不为None，则返回数据库连接对象所创
    建的游标对象；否则返回一个游标对象，该对象是内存中数据
    库连接对象所创建的游标对象'''
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


def close_all(conn, cu):
    '''关闭数据库游标对象和数据库连接对象'''
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()


def drop_table(conn, table):
    '''如果表存在,则删除表，如果表中存在数据的时候，使用该
    方法的时候要慎用！'''
    if table is not None and table != '':
        sql = 'DROP TABLE IF EXISTS ' + table
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu = get_cursor(conn)
        cu.execute(sql)
        conn.commit()
        print('删除数据库表[{}]成功!'.format(table))
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def create_table(conn, sql):
    '''创建数据库表：student'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        conn.commit()
        print('创建数据库表[student]成功!')
        close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))


def drop_table_test():
    '''删除数据库表测试'''
    print('删除数据库表测试...')
    conn = get_conn(DB_FILE_PATH)
    drop_table(conn, TABLE_NAME)


def create_table_test():
    '''创建数据库表测试'''
    print('创建数据库表测试...')
    create_table_sql = '''CREATE TABLE `beautifulGirl` (
                          `id` int(11) NOT NULL,
                          `url` varchar(200) NOT NULL,
                           PRIMARY KEY (`id`)
                        )'''
    conn = get_conn(DB_FILE_PATH)
    create_table(conn, create_table_sql)


def save_test():
    '''保存数据测试...'''
    print('保存数据测试...')
    save_sql = '''INSERT INTO beautifulGirl values (?, ?)'''
    data = imgArrs
    conn = get_conn(DB_FILE_PATH)
    save(conn, save_sql, data)


def save(conn, sql, data):
    '''插入数据'''
    if sql is not None and sql != '':
        if data is not None:
            cu = get_cursor(conn)
            for d in data:
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, d))
                cu.execute(sql, d)
                conn.commit()
            close_all(conn, cu)
    else:
        print('the [{}] is empty or equal None!'.format(sql))



def init():
    '''初始化方法'''
    # 数据库文件绝句路径
    global DB_FILE_PATH
    DB_FILE_PATH = 'beautifulGirl.db'
    # 数据库表名称
    global TABLE_NAME
    TABLE_NAME = 'beautifulGirl'
    # 是否打印sql
    global SHOW_SQL
    SHOW_SQL = True
    print('show_sql : {}'.format(SHOW_SQL))
    # 如果存在数据库表，则删除表
    drop_table_test()
    # 创建数据库表student
    create_table_test()
    # 向数据库表中插入数据
    save_test()

IMGARR = []
# 先获取第一页的数据
dlFir = getImgParent(baseUrl)
# 接着获取第一页的img
IMGARR.append(getImgSrc(dlFir))
# 最后获取下一页的url
nextUrl = getNextPageUrl(dlFir)
# 获取到的图片平摊
imgArrs = []

# 循环判断是否存在下一页，存在的话，获取下一页的数据
while nextUrl:
    # print(nextUrl)
    # 下一页存在的情况下，获取下一页的dl数据
    dlNew = getImgParent(nextUrl)
    # 接着获取下一页的img
    IMGARR.append(getImgSrc(dlNew))
    if len(IMGARR) > 3:
        break
    # 获取下一页的下一页信息
    nextUrl = getNextPageUrl(dlNew)

downLoadImg(IMGARR)
print(IMGARR)