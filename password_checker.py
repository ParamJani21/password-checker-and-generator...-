import random
import string
print("\n**********************************welcome to password checker**********************************\n")
message="Enter the strong password,"
message+="Enter charcter with upper and lower case...!\n"
message+="Also try to add some digit and special symbols for make it strong...!\n-->"

def generator():
    print("\nYou enter very week password let me generate 3 strong password for you...!")
    print("**********************************************************************************")
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case=upper_case.lower()
    digit="0123456789"
    symbol="!@#$%^&*()_+\\?.><,"
    pa=""
    upeer,lower,sym,digi=True,True,True,True
    if upeer:
        pa+=upper_case
    if lower:
        pa+=lower_case
    if digi:
        pa+=digit
    if sym:
        pa+=symbol
    
    length=10
    amount=3

    for p in range(amount):
        password_genrate="".join(random.sample(pa,length))
        print(password_genrate)
    print("**********************************************************************************")
while True:
    password = input(message)


    upper_case=any(1 if c in string.ascii_uppercase else 0 for c in password)
    lower_case=any(1 if c in string.ascii_lowercase else 0 for c in password)
    digit=any(1 if c in string.digits else 0 for c in password)
    special_symbol=any(1 if c in string.punctuation else 0 for c in password)

    charachter=[upper_case,lower_case,special_symbol,digit]

    length = len(password)

    score = 0

    with open("common_pass.txt","r") as f:
        common =f.read().splitlines()
    if password in common:
        print("Password is too common to crack...!")
        

    #length scoring...!

    if length > 8:
        score+=1
    if length > 12:
        score+=1
    if length > 18:
        score+=1

    if sum(charachter) > 1:
        score +=2
    if sum(charachter) > 2:
        score +=1
    if sum(charachter) > 3:
        score +=1

    print(f"Password has {str(sum(charachter))} different character type...!")

    if score <4:
        print("Password is week, there is time to worry about your privacy...!")
        print(f"score is {score}")   
        generator()
    if score==4:
        print("Password is ok...!")
        print(f"score is {score}")   
    if 4<score <6:
        print("Password is good...!")
        print(f"score is {score}")   
    if score >6:    
        print("Password is strong enough to take more time of hacker to gusse this...!")
        print(f"score is {score}")   
    
    dision=input("Enter 1 for continue to check the password othervice enter 0\n-->")

    if dision == 0:
        break

    print("\n")
