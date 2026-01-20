from basic import add
import pytest

def add_three_numbers():
  assert add(5,10,15)==30

def add_two_numbers():
  assert add(2,10)==15
