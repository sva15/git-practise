"""
Tests for utility functions
"""

import sys
sys.path.insert(0, '../src')

from utils import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    print("All tests passed!")
