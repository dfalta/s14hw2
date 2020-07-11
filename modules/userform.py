from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[validators.NumberRange(min=0, max=130)])
    submit = SubmitField('Add')
