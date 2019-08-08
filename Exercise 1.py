#Accept two int values from the user and return their product. If the product is greater than 1000, then return their sum
x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
a = x*y
if a <=1000:
    print(a)
else:
    print(x+y)

