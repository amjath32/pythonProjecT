choice=input("Choose if you want to register(1) or login(2): ")
if int(choice)==1:
    reg=input("Input your email: ")
    passreg1=input("Create your password: ")
    passreg2=input("Confirm your password: ")
    f=open("email.txt","r")
    lines=str(f.read())
    if reg==any(lines):
        print("You already have an account!")
    else:
        if str(passreg1)==str(passreg2):
            #f=open("email.txt", "a")
            #f.write("\n" + reg)
            #f.close()
            print("Account registered successfully.")
        else:
            print("Passwords do not match.")
else:
    log=input("Input your email: ")
    passlog=input("Input your password: ")
    print("Login successful!")