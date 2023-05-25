import requests

def get_weather_in_plases(plases):
    for plase in plases:
        print(get_weather(plase))

def get_weather(plase):
    url = f'https://wttr.in/{plase}'
    payload = {'nTqM': '', 'lang': 'ru'}
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        return response.text
    except:
        return f'Не удалось получить погоду в {plase}'


if __name__ == "__main__":
    plases = ['Лондон', 'Шереметьево', 'Череповец']
    get_weather_in_plases(plases)
