from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CityWeatherForm(FlaskForm):
    city_name = StringField('city', validators=[DataRequired()])
    submit = SubmitField()