from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    age = IntegerField('age', validators=[DataRequired()])
    bmi = DecimalField('bmi', validators=[DataRequired()])
    sex = SelectField('sex', choices=[( 0.50680, 'female'), (-0.044642, 'male')], validators=[DataRequired()])
