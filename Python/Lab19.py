
import os

def save(n):
    f=open("data.txt","w")
    f.write(n)
    f.close()

while True:
    print("1.write/save\n2.display notes\n3.exit")
    ch=input("Enter your choie: ")

    if ch==1:
        notes=input("Enter note: ")
        save(notes)
        
    elif ch==2:
        if os.path.exists("data.txt"):
            f=open("data.txt","r")
            notes=f.read()
            print(notes)
            f.close()
        else:
            print("FILE NOT FOUND")
    elif ch==3:
        break
    else:
        print("INVALID")