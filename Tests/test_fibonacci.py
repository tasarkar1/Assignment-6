import pytest
from fibonacci import Fibonacci

def test_constructor_Valueerror():
    with pytest.raises(ValueError):
        (list(Fibonacci("Hi")))

