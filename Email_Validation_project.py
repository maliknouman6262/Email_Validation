while True:
    print("Welcome to Email Validator")
    
    Email=input("Enter your Email: ")
    if Email=="exit":
        break
    k=0
    j=0
    d=0
    if len(Email) >= 6:
        if Email[0].isalpha():
            if ("@" in Email) and Email.count("@")==1:
                if (Email[-4]==".") ^ (Email[-3]=="."):
                    for i in Email:
                        if i==i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="_" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                    if k==1 or j==1 or d==1:
                        print("wrong email 5")
                else:
                    print("wrong email 4")
            else:
                print("wrong email 3")
        else:
            print("wrong email 1")
    else:
        print("wrong email 2")