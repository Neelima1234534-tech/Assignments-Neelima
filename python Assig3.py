# useing third Variable.
a=10
b=20
c=a
a=b
b=c
print("Value of a:",a)
print("Value of b:",b)
# with out useing third variable.
a=10
b=20
a,b=b,a
print("Value of a:" ,a)
print("Value of b:" ,b)