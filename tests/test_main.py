import pytest
from src.main import add, is_palindrome

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_palindrome():
    assert is_palindrome("radar")
    assert not is_palindrome("hello")
