def calc(x, y):
    return x+y, x-y, x*y, x/y
print("Enter two numbers")
x = int(input())
y = int(input())
add, sub, mul, div = calc(x, y)
print("The sum is", add) 
print("The difference is", sub) 
print("The product is", mul) 
print("The quotient is", div)