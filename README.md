bootl1= True
bootl2= False
print(70==70)
print(3!=3)
print(50>10)
print(14<15)
print(20>=18)
print(35<=34)


#input("my score is:")
print(input)
score= int(input("my score is:"))
if score>50 or score<=100:
    print("passing")
else:
    print("failing")


age= int(input("my age is:"))
if age <18:
    print("minor")
else:
    print("adult")


number1=int(input("number1:"))
number2=int(input("number2:"))
if number1>number2:
    print("number 1 is grater than number2")
elif number1<number2:
    print("number 2 is grater than number1")
else:
    print("they are equal")



pass1=int(input("enter your password:"))
pass2=int(input("enter your password again:"))
if pass1 == pass2 :
    print("confirm")
else:
    print("try again")


    grade=int(input("grade:"))
    if grade >=90:
        print("A")
    elif grade >=80:
        print("B")
    elif grade>=60:
        print("C")
    elif grade>=30:
        print("D")
    else:
        print("F")

    temp=int(input("temperature:"))
    if temp<10:
        print("it is cold")
    elif temp >=10-25:
            print("it is warm")
    else:
        print("it is hot")

    number=int(input("number:"))
    if number<100:
        print("small")
    elif number >=100:
        print("not that small not that big")
    elif number >=1000:
        print("not that small not that big")
    else:
        print("big")

    username=int(input("your username:"))
    password=int(input("your password:"))
    username2="jjj"
    password2="ppp"
    if username==username2:
        print("access granted")
    elif password==password2:
        print("access granted")
    else:
        print("access denied")
