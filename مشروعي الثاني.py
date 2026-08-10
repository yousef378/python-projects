list_of_admins=["yousef","ibrahim","mohamed","adam"]

name=input("your name please:").lower()

if name in list_of_admins:
    print(f"hi {name},welcome back")
    option=input("update or delete:").lower()
    if option == "update":
        new_name=input("your new name please:").lower()
        list_of_admins[list_of_admins.index(name)]=new_name
        print(list_of_admins)
    elif option == "delete":
        list_of_admins.remove(name)
        print(list_of_admins)
    else:
        print("please whrit correct option")
else:
    print("you are not admin")
    option2=input("do you want to add you:").lower()
    if option2 == "yes":
        list_of_admins.append(name)
        print(list_of_admins)
    elif option2 == "no":
        print("ok")
        print(list_of_admins)
    else:
        print("please write yes or no")
