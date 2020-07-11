from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, HiddenField, validators
from wtforms.validators import DataRequired


class EditUserForm(FlaskForm):
    user_id = HiddenField("User Id")
    first_name = StringField('First Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[validators.NumberRange(min=0, max=130)])
    submit = SubmitField('Edit')
