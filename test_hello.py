from hello import add, multiply


def test_add():
    """
    Test the function add
    from the module hello.py
    """

    assert 2 == add(1, 1)
    assert -10 == add(-30, 20)
    assert 0 == add(-1, 1)


def test_multiply():
    """
    Test function multiply
    from the module hello.py
    """

    assert 2 == multiply(1, 2)
    assert 10 == multiply(2, 5)
    assert -30 == multiply(-10, 3)
    assert 100 == multiply(-10, -10)
    assert 0 == multiply(0, 1)
