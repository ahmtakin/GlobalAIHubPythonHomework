name=input("please enter your first name: ")
surname=input("please enter your last name: ")
age=int(input("please enter your age: "))
dateofb=input("please enter your date of birth: ")
userinfo=[name,surname,age,dateofb]
for i in userinfo:
    print(i)
if age <18:
    print("You can't go out it is too dangerous.")
else:
    print("You can go out to the street.")