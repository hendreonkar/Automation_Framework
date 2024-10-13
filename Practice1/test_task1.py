import pytest
@pytest.mark.smoke
def test_test_case1():
    print('Hello Onkar!')

@pytest.mark.smoke
def test_test_case2():
    assert 10+5==13

@pytest.mark.skip(reason= "testing skip")
def test_test_case3():
    assert 10+5==15

@pytest.mark.reg
def test_test_case4():
    print('Hello Admin!')