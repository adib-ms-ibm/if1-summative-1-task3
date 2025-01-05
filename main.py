# Python program to convert arabic numbers to roman numerals

romano_arabiyyahDict = {
  "X̅": 10000,
  "MX̅": 9000,
  "V̅": 5000,
  "MV̅": 4000,
  "M": 1000,
  "CM": 900,
  "D": 500,
  "CD": 400,
  "C": 100,
  "XC": 90,
  "L": 50,
  "XL": 40,
  "X": 10,
  "IX": 9,
  "V": 5,
  "IV": 4,
  "I": 1
}

def arabiyyah_to_roman(arabNum):
  if arabNum <= 0:
    if arabNum == 0:
      return "Ancient Rome did not have a placeholder for zero!"
    else:
      return "Ancient Rome didn't have Chinese knowledge!"

  romanNum = ''
  to_convert = arabNum

  first_kv = romano_arabiyyahDict[
    f'{list(romano_arabiyyahDict.keys())[0]}'
  ]

  greater_than_zero = True if to_convert > 0 else False
  less_than_upper_limit = \
    True if to_convert < (first_kv*4) - 1 \
    else False

  if not less_than_upper_limit:
    return "Arabic number too big!"

  while greater_than_zero and less_than_upper_limit:
    for roman, arabiyyah in romano_arabiyyahDict.items():
      while to_convert >= arabiyyah:
        romanNum += roman
        to_convert -= arabiyyah
      greater_than_zero = True if to_convert > 0 else False
  return romanNum

def main():
  arabic = int(input("Convert to Roman: "))
  print(f"\nArabic:  {arabic}\nRoman:   {arabiyyah_to_roman(arabic)}")

if __name__ == "__main__":
  main()
