list1 = [1,2,3]
list2 = [1,2]

intersection = list(filter(lambda x: x in list1, list2))

print(intersection)

