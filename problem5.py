def func(gap):
    mylist=text.split()
    print(f"List:{mylist}")
    string=",".join(mylist)
    string=string.lower().replace("right","LEFT")
    string=string.replace("left","right")
    string=string.replace("LEFT","left")
    print(string)
    
text=input()
func(text)


