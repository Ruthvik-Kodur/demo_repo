from basic import add
import pytest

def test_add_three_numbers():
  assert add(5,10,15)==30

def test_add_two_numbers():
  assert add(2,10)==15
