import random
import datetime
import os
OWNER_NAME="Mahi"
count=0
def id_generator():
    id=""
    
    for i in range(4):
        id+=str(random.randint(0,9))
    return id
def diary_session():
    
    try:
        message=input("how was your day: ")
        if not os.path.exists("Mynotes"):
            os.mkdir("Mynotes")
        stamp=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        id=id_generator()
        with open("Mynotes/diary.txt","a") as file:
            file.write(f"{id} | {stamp} | {message}\n")
        global count
        count+=1
        print(f"{count} messages are written till now!")
    except Exception as e:
        print("diary not working",e)
if __name__=="__main__":
    diary_session()