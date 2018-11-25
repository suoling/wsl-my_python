import sqlite3
import os

def get_conn(path):
    conn = sqlite3.connect(path)
    if os.path.exists(path) and os.path.isfile(path):
        print('硬盘上面:[{}]'.format(path))
        return conn
    else:
        conn = None
        print('内存上面:[:memory:]')
        return sqlite3.connect(':memory:')


def get_cursor(conn):
    if conn is not None:
        return conn.cursor()
    else:
        return get_conn('').cursor()


def close_all(conn, cu):
    try:
        if cu is not None:
            cu.close()
    finally:
        if cu is not None:
            cu.close()


def fetchall(conn, sql):
    '''查询所有数据'''
    if sql is not None and sql != '':
        cu = get_cursor(conn)
        if SHOW_SQL:
            print('执行sql:[{}]'.format(sql))
        cu.execute(sql)
        r = cu.fetchall()
        return r
        # if len(r) > 0:
        #     for e in range(len(r)):
        #         print(r[e])
    else:
        print('the [{}] is empty or equal None!'.format(sql))



def fetchall_test():
    '''查询所有数据...'''
    print('查询所有数据...')
    fetchall_sql = '''SELECT * FROM beautifulGirl'''
    conn = get_conn(DB_FILE_PATH)
    return fetchall(conn, fetchall_sql)


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
    data = fetchall_test()
    girlData = []
    if len(data) > 0:
        for e in range(len(data)):
            # print('表格数据:', data[e])
            girlData.append({'url': data[e][1], 'id': data[e][0]})
        print('表格数据:', girlData)



init()