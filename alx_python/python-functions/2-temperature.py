def convert_to_celsius(fahrenheit):
  """
  Converts a temperature in Fahrenheit to Celsius.

  Args:
    fahrenheit: The temperature in Fahrenheit.

  Returns:
    The temperature in Celsius.
  """

  celsius = (fahrenheit - 32) * 5 / 9
  return celsius


if __name__ == "__main__":
  fahrenheit = 100
  celsius = convert_to_celsius(fahrenheit)
  print("The temperature in Celsius is:", celsius)
