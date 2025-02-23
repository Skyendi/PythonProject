import requests
import pytest


@pytest.fixture()
def obj_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    yield response['id']
    print(response['id'])
    requests.delete(f'https://api.restful-api.dev/objects/{response["id"]}')


def test_create_pet():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    assert response['name'] == payload['name']


def test_get_pet(obj_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id


def test_put_pet(obj_id):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload).json()
    assert response['name'] == payload['name']


def test_delete_pet(obj_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404
