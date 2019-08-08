#Given a list of ints, return True if first and last number of a list is same
def isFirst_And_Last_Same():

    lst = [3, 4, 5, 8, 9, 3, 5]
    if lst[0] == lst[-1]:
        return True
    else:
        return False

print(isFirst_And_Last_Same())