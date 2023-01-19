def fibonacci(n):
    a=0
    b=1
    if n<0:
        print ("incorrect input:")
    elif n==0:
        print(a)
        return a
    elif n==1:
        print(a,b)
        return b
    else:
        print(a,b,end= "")
    for i in range(n-2):
        c=a+b
        print(c,end="")
        a=b
        b=c
    return b
print("Printing fibonacci series:")
print("=====================")
x=int(input("many numbers you want to display:"))
print("The fibonacci series is:")
fibonacci(x)