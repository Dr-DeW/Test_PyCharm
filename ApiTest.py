import requests
import random


# url = 'https://goweather.herokuapp.com/weather/Moscow'


def get_weather_by_city(cty_name):
    url = 'https://goweather.herokuapp.com/weather/' + cty_name
    weather = requests.get(url).json()
    print(weather)


def get_info_blockchane():
    url = 'https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/walltime-info.json?now='
    a = random.randint(1, 345345)
    b = random.randint(1, 345345)
    c = random.randint(1, 345345)
    url = url + str(a) + '.' + str(b) + '.' + str(c)
    req = requests.get(url).json()
    return req


def get_last_trades_retrieval():
    url = 'https://s3.amazonaws.com/data-production-walltime-info/production/dynamic/meta.json?now='
    a = random.randint(1, 345345)
    b = random.randint(1, 345345)
    c = random.randint(1, 345345)
    url = url + str(a) + '.' + str(b) + '.' + str(c)
    req = requests.get(url).json()
    return req


def get_keys_dict(g):
    l = []
    for i in g.keys():
        l.append(i)
    return l


f = get_last_trades_retrieval()
key = get_keys_dict(f)
print(f)
print(f[key[2]])


