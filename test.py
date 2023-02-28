from urllib.parse import quote
import requests


def test_name():
    name = 'Кариухина Александра Егоровна'
    url = 'http://127.0.0.1:5000/person/{}'.format(quote(name))
    response = requests.get(url)
    data = response.json()
    assert dict(data)['person'] == name
