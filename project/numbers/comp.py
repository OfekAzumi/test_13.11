# Complicated Functions:
#   - SumOfDigits (num) --> function to sum up all of the digits
#   - isPal (num) --> function to check if the numebr is a palindrom (1221, 34543, ...)

def SumOfDigits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def isPal(num):
    i = 0 # digit at the start
    j = len(str(num)) - 1 # digit at the end
    while(i < j): # until crosses the middle
        if (str(num)[i] != str(num)[j]):
            return False
        i+=1
        j-=1
    return True
