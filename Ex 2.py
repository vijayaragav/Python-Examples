#Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number
def sum():
    lst = [2, 4, 8, 5, 90]
    j=0
    print(lst[0])
    for i in lst:
        a = i+j
        print(a)
        j = i
sum()