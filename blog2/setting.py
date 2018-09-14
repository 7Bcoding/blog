
# _*_ coding: utf-8 _*_
import os
#调试模式是否开启
DEBUG = True
APP_DIR = os.path.dirname(os.path.realpath(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/blog'

