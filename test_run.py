import requests
from http import HTTPStatus


def test_index():
    response = requests.get("http://localhost:5000")
    assert response.status_code == HTTPStatus.OK
