import requests

def test_pets_quantity():
    response = requests.get('https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available').json()
    assert len(response) == 91
