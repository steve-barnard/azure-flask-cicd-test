import pytest


def add(x,y):
    return x + y

@pytest.mark.parametrize('x, y, result', [
    (10, 10, 20),
    (5, 5, 10),
    (6, 6, 12)
])
def test_add(x, y, result):
    assert add(x, y) == result
