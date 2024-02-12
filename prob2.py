strings = ['abba','bbb','a', 'bb']

# Sort the list based on the length of strings and alphabetically in case of a tie
sorted_strings = sorted(strings, key = lambda x: x)

print(sorted_strings)