import pytest
from fibonacci import Fibonacci

def test_constructor_one():
    assert (list(Fibonacci(1)))== [0,1]


