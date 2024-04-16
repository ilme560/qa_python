import pytest

from main import BooksCollector

@pytest.fixture
def books():
    books = 'Война и мир'
    return books

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector