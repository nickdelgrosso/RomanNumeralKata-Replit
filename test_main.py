import pytest
from main import from_roman

cases = [
  ('I', 1),
  # ('II', 2),
  # ('III', 3),
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman
