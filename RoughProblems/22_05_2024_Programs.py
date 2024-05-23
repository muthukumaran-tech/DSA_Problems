# Given four inputs that are stored in variables a, b, c, and d. you need to print three arrows made up of a , vertical distance between all three arrows will be length b, the middle arrow will be forward by a horizontal distance of length c. length of the arrow will be d (body) plus 1 for the tip.

# Example 1:

# Input:
# a = '-'
# b = 3
# c = 10
# d = 15

# Output:
# --------------->


#           --------------->


# --------------->
# Explanation: The body of the arrow is made up of a. The length is (d = 15(body))+1(tip).The vertical distance is b = 3, and the middle arrow start with the horizontal distance of c = 10.

def utility():
    #The following 4 lines take the inputs. Don't change them!
    a=input()
    b=int(input())
    c=int(input())
    d=int(input())
    arrow = a*d + ">"
    print(arrow)
    
    # Print the vertical distance gap
    for i in range(b-1):
        print()
    
    # Print the second arrow with horizontal offset
    print(' ' * c + arrow)
    
    # Print the vertical distance gap
    for i in range(b-1):
        print()
    
    # Print the third arrow
    print(arrow)

utility()