## Q1:
def calculate_factorial(n):
  if n < 0:
    return "Factorial is not defined for negative numbers"
  elif n == 0 or n == 1:
    return 1
  else:
    result = 1
    for i in range(2, n + 1):
      result *= i
    return result


userInput = int(input("Enter a positive number: "))
print(calculate_factorial(userInput))

########################################################################


#Q2:she
def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors


userInput = int(input("Enter an integer: "))
print(find_divisors(userInput))

########################################################################


#Q3:
def reverseString(input_string):
  reversed = ""
  for char in input_string:
    reversed = char + reversed
  return reversed


userInput = input("Enter a string: ")
print(reverseString(userInput))

#########################################################################


#Q4:
def filter_even_numbers(input_list):
  even_numbers = []
  for number in input_list:
    if number % 2 == 0:
      even_numbers.append(number)
  return even_numbers


userInput = input("Enter a list of numbers separated by commas: ")
input_list = [int(x) for x in userInput.split(',')]
result = filter_even_numbers(input_list)
print(result)

########################################################################


#Q5:
def strongPassword(password):
  special = "#?!$"
  has_digit = has_upper = has_lower = has_special = False
  if len(password) >= 8:
    for char in password:
      if char.isdigit():
        has_digit = True
      elif char.isupper():
        has_upper = True
      elif char.islower():
        has_lower = True
      elif char in special:
        has_special = True

  if has_digit and has_upper and has_lower and has_special:
    return "Strong Password"
  return "Weak Password"


user_input = input("Enter a password: ")
result = strongPassword(user_input)
print(result)

#######################################################################


#Q6:
def validip(ip):
  octets = ip.split(".")

  if len(octets) != 4:
    return False
  for i in octets:
    if not i.isdigit():
      return False
    octet_val = int(i)
    if octet_val < 0 or octet_val > 255:
      return False
    if len(i) > 1 and i[0] == 0:
      return False
  return True


user_input = input("Enter an IPv4 address: ")
result = validip(user_input)
if result:
  print(f"{user_input} is a valid IPv4 address.")
else:
  print(f"{user_input} is not a valid IPv4 address.")

########################################################################
