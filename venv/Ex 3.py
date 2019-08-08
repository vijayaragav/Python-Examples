#Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number
s = str(input('Enter the string'))

def PrintEvenIndex(str):
    for i in range(0, len(str)-1, 2):
        print(str[i])

PrintEvenIndex(s)