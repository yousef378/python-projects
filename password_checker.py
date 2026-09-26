tries=4
password=123

password_input=int(input("enter password pleaase:"))

while password_input != password:
    tries-= 1
    print(f"pasword is false,you have {"last" if tries==1 else tries}")
    password_input=int(input("enter password pleaase:"))
    if tries==0:
        break
else:
    print("password is true")
    



