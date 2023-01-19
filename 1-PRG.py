def push():
    a=int(input("Enter the marks which you want to push:"))
    stack.append(a)
    return a
def pop():
    if stack==[]:
        print(" Stack empty....Underflow case....can not delete the element...")
    else:
        print("deleted mark is :",stack.pop())
def display():
    if stack==[]:
        print(" Stack empty....no elements in stack..")
    else:
        for i in range(len(stack)-l,-l,-l):
            print(stack[i])
stack=[]
print("STACK OPERATIONS")
print("*************")
choice="y"
while choice=="y":
    print("1.PUSH")
    print("2.POP")
    print("3.DISPLAY ELEMENTS OF STACK")
    print("************************")
    c=int(input("Enter your choice : "))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    else:
        print("wrong input:")
    Choice=input("Do you want to continue or not?(y/n):")