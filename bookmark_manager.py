print("*"*20+"bookmark manager"+"*"*20)

list_of_bookmarks=[]

maximum= 6

while maximum >0:
    web=input("enter a web name without https:// :").lower()
    list_of_bookmarks.append(f"https://{web}")
    maximum-=1
    print(f"website added,you can add {maximum} more")
    print(list_of_bookmarks)
else:
    print(list_of_bookmarks)
    print("bookmark manager is full")

if len(list_of_bookmarks) > 0:
    list_of_bookmarks.sort()
    print("printing your bookmarks")
    index=0
    while index < len(list_of_bookmarks):
        print(list_of_bookmarks[index])
        index+=1
  