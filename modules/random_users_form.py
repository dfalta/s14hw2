from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired


class RandomUsersForm(FlaskForm):
    n_users = IntegerField('Number of Random Users (Max 10)', validators=[validators.NumberRange(min=1, max=10)])
    submit = SubmitField('Add')
