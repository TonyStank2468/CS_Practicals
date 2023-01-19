print ("DISPLAY FILE CONTENT LINE BY LINE WITH EACH WORD SEPARATED BY #")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

a = open(r"C:\Users\Jennifer\Desktop\my project\test 1\output\Text.txt","r")
l = a.readlines()
for line in l:
 x = line.split()
 for y in x:
    print(y+" # ",end = " ")
 print("")