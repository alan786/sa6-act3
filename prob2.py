strings = ['abba','bbb','a', 'bb']

# Sort the list based on the length of strings 
sorted_strings = sorted(strings, key = lambda x: len(x))

print(sorted_strings)