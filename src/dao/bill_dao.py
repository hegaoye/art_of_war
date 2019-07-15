# coding=utf-8
from src.base.databasetools import Sqlite3Tools


class BillDao:
    def __init__(self):
        self.db = Sqlite3Tools()

    def load(self, order_no):
        """
        查询一个订单号
        :param order_no: 订单号
        :return: Bill
        """
        sql = 'select * from bill where order_no="' + order_no + '"'
        return self.db.load(sql)

    def insert(self, order_no, user, money, state, md5, order_time):
        """
        保存订单记录
        :param order_no: 支付订单号
        :param user: 支付者
        :param money: 支付金额
        :param state: 支付状态
        :param md5: md5值
        :param order_time: 交易时间
        :return:
        """
        sql = "insert into bill('order_no','user','money','state','md5','order_time') " \
              "VALUES ('" + str(order_no) + "','" + str(user) + "','" + str(money) + "','" \
              + str(state) + "','" + str(md5) + "','" + str(order_time) + "') "
        self.db.insert(sql)
