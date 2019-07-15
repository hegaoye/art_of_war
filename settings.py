# coding=utf-8
"""
配置上下文 文件
注意配置文件变量必须大写否则错误
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# pitop 配置文件
PITOP_CONF = os.path.join(_basedir, 'sys.conf')

# cachedata 缓存文件
CACHEDATA_JSON = os.path.join(_basedir, 'cachedata.json')

# 数据库配置
DATABASE_PATH = os.path.join(_basedir, 'data.db')

del os
