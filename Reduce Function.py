from functools import reduce

# Example 1: Finding the sum of a list
result = reduce(lambda x, y: x + y, [1, 2, 3])
print(result)  # Output: 6

# Example 2: Using an initial value
result_with_initial = reduce(lambda x, y: x + y, [1, 2, 3], -3)
print(result_with_initial)  # Output: 3

# Example 3: Using the reduce() function with another function (gcd from fractions module)
from fractions import gcd
result_gcd = reduce(gcd, [2, 4, 8], 3)
print(result_gcd)  # Output: 1
