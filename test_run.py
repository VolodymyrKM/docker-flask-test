import pytest
from run import app


@pytest.fixture
def test_cli():
    return app.test_client()


def test_index(test_cli):
    response = test_cli.get("/")
    assert response.status_code == 200


def test_index_response(test_cli):
    response = test_cli.get("/")
    assert response.data == b"<h1> Hello world 3 </h1>"
