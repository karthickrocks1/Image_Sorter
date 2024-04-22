def find_first_numbers(text):
  """
  This function finds the first group of consecutive digits in a string, i.e. the date of photo in this case.

  Args:
      text: The string to search for numbers.

  Returns:
      A string containing the first group of digits found, or None if no digits are found.
  """
  digits = ""
  for char in text:
    if char.isdigit():
      digits += char
    elif digits:
      break  # Stop if a non-digit follows a digit
  return digits