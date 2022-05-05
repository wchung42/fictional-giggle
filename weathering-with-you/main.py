from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')

app = Flask(__name__)

@app.route('/')
def get_home():
    return render_template('index.html')


@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        
    try:
        resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={OPEN_WEATHER_API_KEY}')
        resp.raise_for_status()
        content = resp.json()
        lat, long = content[0]['lat'], content[0]['lon']
    except requests.HTTPError as err:
        return f'<p>{err}</p>'

    try:
        resp = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={OPEN_WEATHER_API_KEY}&units=imperial')
        resp.raise_for_status()
        content = resp.json()

        data = {
            'city': city,
            'weather': content['current']['weather'][0]['main'],
            'description': content['current']['weather'][0]['description'],
            'icon': f"http://openweathermap.org/img/wn/{content['current']['weather'][0]['icon']}@2x.png",
            'temp': int(content['current']['temp']),
            'feels_like': int(content['current']['feels_like']),
            'temp_min': int(content['daily'][0]['temp']['min']),
            'temp_max': int(content['daily'][0]['temp']['max']),
            'pressure': content['current']['pressure'],
            'humidity': content['current']['humidity'],
        }
    except requests.HTTPError as err:
        return f'<p>{err}</p>'

    return render_template('weather.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)