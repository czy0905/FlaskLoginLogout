from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('用户名',validators=[DataRequired()])
	password = PasswordField('密码',validators=[DataRequired()])
	remember_me = BooleanField('记住我')
	submit = SubmitField('登录')
