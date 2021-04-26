from app import app
from flask import render_template, request
from app.forms import CityWeatherForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CityWeatherForm()
    city_data = None
    if request.method == 'POST' and form.validate():
        city = form.city_name.data
        api = OpenweatherAPI()
        city_data =  api.get_city_weather_data(city)
    return render_template("index.HTML", form=form, city_data=city_data)