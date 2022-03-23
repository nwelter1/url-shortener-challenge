from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class URLInputForm(FlaskForm):
    link = StringField('Link to shorten', validators=[DataRequired(), URL(message='Please enter a valid URL!')])
    submit_button = SubmitField('Submit')