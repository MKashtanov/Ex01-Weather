import requests

def print_weather_in_places(places):
    for place in places:
        try:
            weather = get_weather(place)
            print(weather)
        except requests.HTTPError:
            print(f'Не удалось получить погоду в {place}')
        except requests.exceptions.ConnectionError:
            print(f'Не удалось подключиться к сайту погоды')

def get_weather(place):
    url = f'https://wttr.in/{place}'
    payload = {'nTqM': '', 'lang': 'ru'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    places = ['Лондон', 'Шереметьево', 'Череповец']
    print_weather_in_places(places)
