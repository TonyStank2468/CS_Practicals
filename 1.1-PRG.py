def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False
def add(atk,item):
    atk.append(item)
    top = len(atk)-1
    
def remove(stk):
    if(atk==[]):
        print('Stack empty;Underflow')
    else:
        print("Deleted student is:",stk.pop())
        
def display(atk):
    if isEmpty(atk):
        print("stack empty")
    else:
        top = len(atk)-1
        print(atk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(atk[a])
            
stack=[]
top = None
while True:
    print("STACK OPERATION:")
    print("1.ADD STUDENT")
    print("2.DISPLAY STACK")
    print("3.REMOVE STUDENT")
    print("4.EXIT")
    ch = int(input("enter your choice(1-4):"))
    if ch== 1:
        rno = int(input("enter roll number:"))
        sname = input("enter student name:")
        item = [rno,sname]
        add(stack,item)
        input()
    elif ch==2:
        display(stack)
        input()