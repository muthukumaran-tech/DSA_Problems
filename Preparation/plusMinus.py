# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

def plusMinus(arr):
    # Write your code here
    length=len(arr)
    p = sum(1 for i in arr if i>0)
    n = sum(1 for i in arr if i<0)
    z = sum(1 for i in arr if i==0)
    print("{:.6f}\n{:.6f}\n{:.6f}".format(p/length,n/length,z/length))

plusMinus([0, 0, -1, 1, 1])

