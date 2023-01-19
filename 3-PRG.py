import pickle
def create():
    list_of_students=[]
    no_of_students=int(input("Enter no of Students:"))
    for i in range(no_of_students):
        roll_no=int(input("Enter roll no:"))
        name=input("Enter name:")
        li=[roll_no,name]
        list_of_students.append(li)
        file=open("C:/Users/Jennifer/Desktop/CSC Programs/output/Students.dat","wb")
        pickle.dump(list_of_students,file)
        print("Data added successfully")
        file.close()
        
def search():
    file=open("C:/Users/Jennifer/Desktop/CSC Programs/output/Students.dat","rb")
    list_of_students=pickle.load(file)
    roll_no=int(input("Enter roll no. of student to search:"))
    found=false
    for stud_data in list_of_students:
        if(stud_data[0]==roll_no):
            found=True
            print("search element found",stud_data[0],stud_data[1])
    if(found==False):
        print("No student data found, please try again")
    file.clos()
    
create()
search()
