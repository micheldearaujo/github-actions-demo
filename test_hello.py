from hello import add


def test_add():
    """
    Test the function hello
    from the module hello.py
    """

    assert 2 == add(1, 1)
    assert -10 == add(-30, 20)
    assert 0 == add(-1, 1)

