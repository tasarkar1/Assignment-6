import pytest
from fibonacci import Fibonacci

def test_constructor_four():
    assert (list(Fibonacci(4)))== [0, 1, 1, 2, 3]


