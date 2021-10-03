a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=(input("choose operator: +,-,*,/: "))
print("\n")
if c=="+":
    print("Sum is", a+b)
elif c=="-":
    print("Subtraction is", a-b)
elif c=="*":
    print("mu;tiplication is", a*b)
elif c=="/":
    print("division is", a/b)
else:
    print("invalid input")
