file=open("C:/Users/Jennifer/Desktop/CSC Programs/output/OP-2-PRG.txt","r")
content=file.read()
vowels=0
consonants=0
lower_case_letters=0
upper_case_letters=0
for ch in content:
    if(ch.islower()):
        lower_case_letters+=1
        
    elif(ch.isupper()):
        upper_case_letters+=1
        
ch=ch.lower()
if(ch in ['a','e','i','o','u']):
    vowels+=1
    
elif(ch in['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']):
    consonants+=1
file.close()

print("Vowels are :",vowels)
print("Consonants :",consonants)
print("Lower_case_letters :",lower_case_letters)
print("Upper_case_letters :",upper_case_letters)