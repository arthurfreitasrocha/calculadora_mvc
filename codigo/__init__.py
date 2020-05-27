def sub(*numbers):
  value = 0

  for number in numbers:
    value -= number

  return value

def sum(*numbers):
  value = 0

  for number in numbers:
    value += number

  return value