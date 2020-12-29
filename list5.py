list1 = [11,23,45,23,64,22,11,24]
# lambda exp.
odd_no = list(filter(lambda x: (x % 2 == 1), list1))
print("odd numbers in the list: ", odd_no)