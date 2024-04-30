# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# number_to_string(67), '67'
# number_to_string(79585), '79585'
# number_to_string(79585), "79585"
# number_to_string(1+2), '3'
# number_to_string(1-2), '-1'

def number_to_string(num):
  string = str(num)
  return string

print(number_to_string(67))