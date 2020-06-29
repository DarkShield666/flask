#!/usr/bin/python
# -*- coding: utf-8 -*-

# config.py

# 配置 sqlalchemy  "数据库+数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码"

# database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '172.20.0.134'
PORT = '9301'
DATABASE = 'checkdata'

# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@172.20.0.134:9301/checkdata"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

DATABASE_BINDS = "{}+{}://{}:{}@{}:{}/".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT)

SQLALCHEMY_BINDS = {
    "db_iris": DATABASE_BINDS + 'db_iris',
    "test": DATABASE_BINDS + 'test'
}

SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-sqlacodegen --flask 'mysql+pymysql://root:123456@172.20.0.134:9301/checkdata'
# flask-sqlacodegen --flask 'mysql+pymysql://root:123456@172.20.0.13:9301/db_iris'
