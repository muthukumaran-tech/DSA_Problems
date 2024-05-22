
#using temp variable
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


#using comma variable

def swap(a,b):
    a,b = b,a
    return a,b

# using without temp

def swap(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

print(swap(10,50))

# Equality Operator vs Identiy Operator

a = 10
b=10
c=a
print(a==b)
print(c is b)