from django.shortcuts import render
import requests
from .models import City

# Create your views here.


def home(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=42eeaefffa401d6edad4e13e4acfaff4'
    city = 'Dhaka'

    cities = City.objects.all()

    # to store all dic
    weather_data = []

    for city in cities:
        # writing the request var which fetch data
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city,
            'temparature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],

        }
        print(city_weather)
        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data}

    return render(request, 'weather.html', context)
