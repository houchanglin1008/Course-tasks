# -*- encoding:utf-8 -*-
import requests
import time
import json
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pandas as pd
import pymysql

header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36 SLBrowser/6.0.1.9171'
}

db = pymysql.connect("localhost", "root", "150207", "hao1", charset='gbk')  # 连接数据库
cursor = db.cursor()


# 生成366天的时间表
def dateRange(a):
    fmt = '%Y-%m-%d'
    bgn = int(datetime.strptime(a, fmt).timestamp())  # 转化为时间戳
    end = int(datetime.now().timestamp())
    list_date = [datetime.strftime(datetime.fromtimestamp(i), fmt) for i in range(bgn, end + 1, 3600 * 24)]
    # 用一天3600*24秒作为步长，转化为日期格式
    return list_date


# 获取每个地区的名称和地区ID
def get_id():
    url = "https://hangqing.zhuwang.cc/zhurou/index.html"
    r = requests.get(url,headers=header)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('body > div.main > div.mainr > div:nth-child(1) > div.shengshi > a ')
    province_id = []  # 用BeautifulSoup解析网页源码
    province_name = []
    cursor.execute("drop table if exists province")
    sql = "create table province (\
            Province varchar(20) not null,\
            Province_id int(20) not null)"
    cursor.execute(sql)        
    cursor.execute("alter table province convert to character set utf8mb4;")
    db.commit()
    for item in data:
        pro_name = item.get_text()
        pro_id = re.findall(r'\d+', item.get("href"))
        province_name.append(pro_name)
        province_id.append(pro_id[0])
        sql = "insert into province values('" + pro_name + "','" + pro_id[0] +"');"
        cursor.execute(sql)
        db.commit()
    return [province_name, province_id]


def get_data(province_id):
    dic = {}
    url = "https://zhujia.zhuwang.cc/api/chartData?areaId={}".format(province_id)
    html = requests.get(url,headers=header)
    html.encoding = 'utf8'
    doc = html.json()  # 获取json格式数据
    a = '-'.join(doc['time'][3])
    dic['pigprice'] = doc['pigprice']
    dic['pig_in'] = doc['pig_in']
    dic['pig_local'] = doc['pig_local']
    dic['maize'] = doc['maizeprice']
    dic['bean'] = doc['bean']
    dic['time'] = dateRange(a)
    return dic



# 将数据存入MySQL数据库
def save_data(dic,province_name,pro_no):
    cursor.execute("drop table if exists price%s;" %pro_no)
    sql = "create table price%s" %pro_no +\
        " (Province varchar(20) not null,\
            Pigprice float(20) not null,\
            Pig_in float(20) not null,\
            Pig_local float(20) not null,\
            Maize float(20) not null,\
            Bean float(20) not null,\
            Time date not null)"
    cursor.execute(sql)
    cursor.execute("alter table price%s convert to character set utf8mb4;"%pro_no)
    db.commit()
    count = len(dic['time'])
    for i in range(count):
        Province = province_name
        Pigprice = str(dic['pigprice'][i])
        Pig_in = str(dic['pig_in'][i])
        Pig_local = str(dic['pig_local'][i])
        Maize = str(dic['maize'][i])
        Bean = str(dic['bean'][i])
        Time = dic['time'][i]
        print(Province,Pigprice, Pig_in, Pig_local, Maize, Bean, Time)
        sql = "insert into price%s"%pro_no +" values('" + Province + "','" + Pigprice + "','" + Pig_in + "',\
        '" + Pig_local + "','" +Maize + "','" + Bean + "','" + Time + "');"
        cursor.execute(sql)
        db.commit()
def get_china():
    dic = {}
    url = "https://zhujia.zhuwang.cc/api/chartData/"
    html = requests.get(url)
    html.encoding = 'utf8'
    doc = html.json()  # 获取json格式数据
    a = '-'.join(doc['time'][3])
    dic['pigprice'] = doc['pigprice']
    dic['pig_in'] = doc['pig_in']
    dic['pig_local'] = doc['pig_local']
    dic['maize'] = doc['maizeprice']
    dic['bean'] = doc['bean']
    dic['time'] = dateRange(a)
    return dic

def save(dic):
    cursor.execute("drop table if exists price")
    sql = "create table price\
            (Pigprice float(20) not null,\
            Pig_in float(20) not null,\
            Pig_local float(20) not null,\
            Maize float(20) not null,\
            Bean float(20) not null,\
            Time date not null)"
    cursor.execute(sql)
    db.commit()
    count = len(dic['time'])
    for i in range(count):
        Pigprice = str(dic['pigprice'][i])
        Pig_in = str(dic['pig_in'][i])
        Pig_local = str(dic['pig_local'][i])
        Maize = str(dic['maize'][i])
        Bean = str(dic['bean'][i])
        Time = dic['time'][i]
        print(Pigprice, Pig_in, Pig_local, Maize, Bean, Time)
        sql = "insert into price values('" + Pigprice + "','" + Pig_in + "',\
        '" + Pig_local + "','" +Maize + "','" + Bean + "','" + Time + "');"
        cursor.execute(sql)
        db.commit()

def main():
    province = get_id()
    pro_num = len(province[0])
    for i in range(pro_num):
        time.sleep(2)
        pro_name = province[0][i]
        pro_no = province[1][i]
        dic = get_data(province[1][i])
        save_data(dic, pro_name,pro_no)
        print('%s' % pro_name + '\t生猪价格数据存储完毕')
    


if __name__ == "__main__":
    main()
    time.sleep(2)
    save(get_china())
    db.close()
    print('\n保存完毕')