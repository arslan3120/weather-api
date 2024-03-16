from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def fetch_weather(city):
    API_KEY = '94bc52b857f365d91de53f87a2e9de76'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@app.route("/weather", methods=['GET'])
def get_weather():
    city = request.args.get('city') 

    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_data = fetch_weather(city)

    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
