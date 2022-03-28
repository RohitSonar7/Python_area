import Calculations

def test_RectangleArea():
    x = 10
    y = 20
    result = Calculations.RectangleArea(x , y)
    assert x * y == result
def test_ReactanglePeri():
    x = 10
    y = 20
    result = Calculations.RectanglePeri(x , y)
    assert  x + x + y + y == result
def test_SquareArea():
    x = 10
    result = Calculations.SquareArea(x)
    assert x * x == result
