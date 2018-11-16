import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask,request,current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = '请先登录以进入该页面'

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	db.init_app(app)
	login.init_app(app)

	from app.auth import bp as auth_bp
	app.register_blueprint(auth_bp, url_prefix='/auth')
	
	from app.main import bp as main_bp
	app.register_blueprint(main_bp)
	
	if not app.debug and not app.testing:
		if not os.path.exists('logs'):
			os.mkdir('logs')
		file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
		file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s:%(message)s''[in %(pathname)s:%(lineno)d]'))
		file_handler.setLevel(logging.INFO)
		app.logger.addHandler(file_handler)
		
		app.logger.setLevel(logging.INFO)
		app.logger.info('程序启动')
	return app

from app import models
