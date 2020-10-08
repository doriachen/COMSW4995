#import the method from project folder
from my_test_proj import inc

#define test method
def test_inc():
    assert inc(1) == 2
