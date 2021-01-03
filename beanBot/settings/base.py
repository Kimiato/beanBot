# 这是基本的配置文件
# 可以将其修改为你需要的配置
from nonebot.default_config import *


# beanBot所使用的监听端口和ip, 需要和 mirai-http 的配置对应

PORT = 9000
HOST = '127.0.0.1'  # 本地部署所使用的ip

SUPERUSERS = []  # 超级管理用户，如果有多个请用半角逗号","隔开

COMMAND_START = {''}  # 命令前缀，如果有多个请用半角逗号","隔开

PLUGINS = ['']

# 数据库设置
DATABASE_SETTINGS = {
    'ENGINE': 'sqlite',  # 可以选择sqlite或者mysql, sqlite可以不用填写下面的NAME, USER, PASSWORD, HOST, PORT配置
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': ''
}