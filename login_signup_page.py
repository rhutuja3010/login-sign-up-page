import json
import os

print("...**...WELCOME TO LOGIN AND SIGN UP PAGE...**...")
def signuppassword(password):
    if len(password)>=8 or len(password)<=18:
        if password>="a" and password<="z":
            if  "@" in password or "#" in password :
                if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or  "0" in password:
                    print("it is strong password")
                else:
                    print("wrong password")
                    password=(input("enter the password  : "))
                    signuppassword(password)
            else:
                print("incorrect special chr")
                password=(input("enter the password  : "))
                signuppassword(password)
        else:
            print("incorrect  alp")
            password=(input("enter the password  : "))
            signuppassword(password)
    else:
        print("out of length")
        password=(input("enter the password  : "))
        signuppassword(password)
    
def confirmpassword(password,password1):
    if password==password1:
        print("write password")
    else:
        print("cornfirm password is wrong")
        password1=input("again enter the password1")

user=input("you want to do login or signup :")
file=os.path.exists("signup.json")
if file==False:
    if user=="signup":
        username=input("enter the username :")
        password=input("enter the password  :")
        signuppassword(password)
        password1 =input("enter the password confirm password :")
        confirmpassword(password,password1)
        print("congrats",username,"you are signed up successfully")
        date_of_birth=(input("enter the date of birth"))
        hobby=input("enter the hobbys :")
        gender=input("enter the gender :")
        description=input("enter the description :")   
        mylist=[]
        information={}
        name=["username","password","date_of_birth","hobby","gender","description"]
        infor=[username,password,date_of_birth,hobby,gender,description]
        for i in range(len(name)):
            information.update({name[i]:infor[i]})
        mylist.append(information)
        with open("signup.json","a") as f:
            json.dump(mylist,f,indent=2)
elif file==True:
    if user=="signup":
        username=input("enter the username :")
        password=input("enter the password :")
        signuppassword(password)
        password1 =input("enter the password confirm password :")
        confirmpassword(password,password1)
        r=open("signup.json","r")
        username1=r.read()
        if username in username1:
            print("name is already exists")
        else:
            print("congrats",username,"you are signed up successfully")
            date_of_birth=(input("enter the date of birth"))
            hobby=input("enter the hobbys :")
            gender=input("enter the gender :")
            description=input("enter the description :") 
            information={}
            name=["username","password","date_of_birth","hobby","gender","description"]
            infor=[username,password,date_of_birth,hobby,gender,description]
            for i in range(len(name)):
                information.update({name[i]:infor[i]})

            with open("signup.json","r")as f :
                data=json.load(f)
                data.append(information)
                with open("signup.json","w") as f:
                    json.dump(data,f,indent=2)
    elif user=="login":
        username2=input("enter the username :")
        password2=input("enter the password :")
        with open("signup.json","r") as f:
            data=json.load(f)
            for i in range(len(data)):
                if data[i]["username"]==username2:
                    if data[i]["password"]==password2:
                        print("login successfully")
                        print("Your Name is",data[i]["username"],"\n")
                        print("and your data is :- \n")
                        for x,y in data[i].items():
                            print("your",x,"is",y)
                            
                    else:
                        print("wrong")
                        break
            


            

