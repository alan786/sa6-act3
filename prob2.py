strings = ['abba','bbb','a', 'ab']

# Sorting the list based on length and then alphabetically
sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted list:", sorted_strings)
