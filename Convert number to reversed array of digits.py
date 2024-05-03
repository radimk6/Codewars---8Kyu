# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

# def basic_test_cases():
#         test.assert_equals(digitize(35231),[1,3,2,5,3])
#         test.assert_equals(digitize(0),[0])

def digitize(n):
    n = str(n)
    numbers = []
    for one_number in n:
        numbers.append(int(one_number))
    numbers.reverse()
    return numbers

print(digitize(35231))