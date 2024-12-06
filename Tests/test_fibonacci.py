import pytest
from fibonacci import Fibonacci

def test_constructor_two():
    assert (list(Fibonacci(2)))== [0,1,1]


