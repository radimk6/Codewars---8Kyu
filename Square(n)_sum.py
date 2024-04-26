# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because (1**2 + 2**2 + 2**2 = 9)

# test.assert_equals(square_sum([1,2]), 5)
# test.assert_equals(square_sum([0, 3, 4, 5]), 50)
# test.assert_equals(square_sum([]), 0)
# test.assert_equals(square_sum([-1,-2]), 5)
# test.assert_equals(square_sum([-1,0,1]), 2)


def square_sum(numbers):
  result = 0
  for x in numbers:
    result += x**2
    
  return result

num = [-1, 0, 1]
square_sum(num)


