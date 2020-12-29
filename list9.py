#dictionary that contains numbers in the form of x:x**x
number = int(input(" enter the number : "))

Dict = {x:x * x for x in range(1, number + 1)}

print("Dictionary = ", Dict)