import pymysql
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect("localhost", "root", "150207", "hao1", charset='gbk')
            self.cursor = self.conn.cursor()
            print("连接数据库成功")
        except:
            print("数据库连接失败")

    def get_pro_id(self):
        sql = 'select * from province'    
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values

    def get_map_Items(self,pro_id):
        sql = 'select * from price%s' %pro_id     
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values

    def get_l1_Items(self):
        sql = 'select * from price'  
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values


if __name__=="__main__":
    pass