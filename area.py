a=float(input("enter a first number:"))
b=float(input("enter a second number:"))
c=float(input("enter a third number:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print('the area of the triangle is %0.2f' %area)