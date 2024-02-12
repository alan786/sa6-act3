from functools import reduce

numbers = [3, 7, 2, 9, 5, 1]

# Use reduce with a lambda function to find the maximum number in the list
max_num = reduce(lambda x, y: x if x >= y else y, numbers)

print("Maximum number in the list:", max_num)

