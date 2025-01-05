# Unit tests for Arabiyyah-Romano Converter written with Pytest

from main import arabiyyah_to_roman

def test_zero():
  assert arabiyyah_to_roman(0) == "Ancient Rome did not have a placeholder for zero!"

def test_upper_limit():
  assert arabiyyah_to_roman(39999) == "Arabic number too big!"

def test_negative_int():
  assert arabiyyah_to_roman(-1) == "Ancient Rome didn't have Chinese knowledge!"

def test_romano_arabiyyah():
  test_cases = [
    (1, "I"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M"),
    (4000, "MV̅"),
    (5000, "V̅"),
    (9000, "MX̅"),
    (10000, "X̅")
  ]
  for arabic, expected in test_cases:
    assert arabiyyah_to_roman(arabic) == expected

def test_complicated_numbers():
  test_cases = [
    (40, "XL"),
    (449, "CDXLIX"),
    (499, "CDXCIX"),
    (3999, "MMMCMXCIX"),
    (2024, "MMXXIV"),
    (3888, "MMMDCCCLXXXVIII")
  ]
  for arabic, expected in test_cases:
    assert arabiyyah_to_roman(arabic) == expected
