from django.shortcuts import render
import requests

def index(request):
    app_id = '302451bcef9dde4345085d9a8d8758ab'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id

    city = 'London'
    res = requests.get(url.format(city)).json()
    
    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather']['icon'],
    }

    context = {
        'info': city.info
    }
    return render(request, 'weather/index.html', context)
