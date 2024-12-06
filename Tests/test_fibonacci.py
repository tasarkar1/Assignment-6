import pytest
from fibonacci import Fibonacci

def test_constructor_zero():
    assert (list(Fibonacci(0)))== [0]


