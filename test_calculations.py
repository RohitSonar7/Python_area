import Calculations
import pytest

def test_RectangleArea():
    x = 10
    y = 20
    result = Calculations.RectangleArea(x , y)
    assert x * y == result

@pytest.mark.myproject
def test_ReactanglePeri():
    x = 10
    y = 20
    result = Calculations.RectanglePeri(x , y)
    assert  x + x + y + y == result

@pytest.mark.myproject
def test_SquareArea():
    x = 10
    result = Calculations.SquareArea(x)
    assert x * x == result
