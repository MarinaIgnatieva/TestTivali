import pytest
import requests


@pytest.fixture(scope="session")
def session():
    session=requests.Session()
    yield session
    session.close()

