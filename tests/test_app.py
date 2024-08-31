from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_return_ok():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}  # Assert
