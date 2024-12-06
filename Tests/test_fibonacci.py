import pytest
from fibonacci import Fibonacci

def test_constructor_negative():
    assert (list(Fibonacci(-1)))==  []


