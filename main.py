import pytest


# Source Code:

def from_roman(num: int) -> str:
  return 'a'



# Tests: 

cases = [
  (1, 'I'),
  # (2, 'II'),
  # (3, 'III'),
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman
