import random
import string
while True:
    print("1 : -> 1234567890")
    print("2 : -> abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("3 : -> 1234567890 and abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("4 : ->",string.ascii_letters+string.digits+string.punctuation)

    while True:
        type=input("Enter the type of password need to generate : ")
        if type.isnumeric():
            if int(type)>4 or int(type)<1:
                print("invalid option")
            else:
                break
        else:
            print("ivalid option")

    if (type=="1"):
        charvalues=string.digits
    elif (type=="2"):
        charvalues=string.ascii_letters
    elif (type=="3"):
        charvalues=string.ascii_letters+string.digits
    else:
        charvalues=string.ascii_letters+string.digits+string.punctuation

    length=int(input("Enter the length of password (max-20): "))

    def random_generate(length,charvalues):

        password=[]
        while len(password)!=length:
            password.append(random.choice(charvalues))
        gap=((20-length)*" ")
        print("+-----------------------------------------------------+")
        print("|Randomly generated password : ","".join(password),gap,"|")
        print("+-----------------------------------------------------+")
        print("_____________________________________________________")

    random_generate(length,charvalues)
    rechange="-1"
    while rechange!="0":

        rechange=(input("Enter : 1 \nfor Regenerating the password \n         or \nEnter : 0 \nfor quit \n Enter 10 for main menu\n --->: "))
        
        if rechange=="10":
            break
        if rechange=="1":
            random_generate(length,charvalues)
        elif rechange=="0":
            break
        else:
            print("-----------Invalid Enter------------")
    if rechange=="0":
        break
print("-----------Thankyou for visiting ---------")
print("------------------------------------------")
