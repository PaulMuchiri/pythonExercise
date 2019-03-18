#if else in python
print(" in this world there are two things involved, either you are a 1.man, or 2.woman")
choice = input(">")
#conditin for man
if choice == "1":
    print("if you are a man there are three things involved, its either you are 1.Rich 2.Middle class or 3.Poor")
    choice = input(">")
    #condition for rich
    if choice == "1":
        print("if you are rich there are two things involve is either you marry an 1.educated woman or 2.uneducated woman")
        choice = input(">")
        #educated woman married
        if choice == "1":
            print("you will Have stress and Die!!!!!!!!")
        elif choice == "2":
            print("You will get tired and Die")
        else:
            print("seems You are Burney, Youll not die")
    #conditin middle        
    elif choice == "2":
        print("you will live happy ever after ")
    elif choice == "3":
        print("Man,,,, Dont think About it!!!")
    else:
        print("Wrong input. enter option 1, 2 or 3")
#condition for woman       
elif choice == "2":
    print("if you are a woman there are three things involved, its either you are 1.rich 2.middle class or 3.Poor")


    
    choice = input(">")
    if choice == "1":
        print("you Will not Get married")
    elif choice == "2":
        print("Youll get married, and many kids")
    elif choice =="3":
        print ("Youll get Married to a Rich and Good man.... ")
    else:
        print ("invalid Input, Select option 1, 2 or 3")

else:
    print("invalid choice. Select option 1 or 2")
choice1 = input(">")

    