from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('blog2.setting')     #模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')   #环境变量，指向配置文件setting的路径

#创建数据库对象
db = SQLAlchemy(app)

from blog2.controller import blog_message
from blog2.model import User,Category
