global userreal
global passreal
global keycode

userreal = 'scs'
passreal = 'python'
keycode = '1401'

def userafter():

    print("Login Portal:")
    print("")

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        passwordafter()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userafter()
        
def passwordafter():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        loggedinname()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordafter()

def user():

    print("Login Portal:")
    print("")

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        password()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        user()
        
def password():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        loggedinfirst()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        password()
        
def userkeycode():

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        passwordkeycode()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userkeycode()
        
def passwordkeycode():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        resetkeycodecontinue()()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordkeycode()
        
def userpasscode():

    userinput=input("Username? ")
    
    if userinput == userreal:
        print("")
        passwordpasscode()
    else:
        print("")
        print("There is no user with that username. Try again.")
        print("")
        userpasscode()
        
def passwordpasscode():
    
    passwordinput=input("Password? ")
    
    if passwordinput == passreal:
        print("")
        print("Loading you in...")
        print("")
        resetpasscodecontinue()()
    else:
        print("")
        print("Wrong! Try again.")
        print("")
        passwordpasscode()
        
def loggedinfirst():
    
    global nameuser
    
    nameuser=input("What is your name? ")
    print("")
    loggedinname()
    
def loggedinname():
    
    print("Hello " +nameuser+ "!")
    print("")
    loggedin()
    
def loggedin():
    
    print("Enter '1' to access your file vault.")
    print("Enter '2' to reset your password.")
    print("Enter '3' to reset your keycode.")
    print("Enter '4' to log out.")
    print("")
    
    loggedinmenu=input("Enter your number choice: ")
    print("")
    
    if loggedinmenu == '1':
        
        vaultstart()
        
    elif loggedinmenu == '2':
        
        resetpassword()
        
    elif loggedinmenu == '3':
        
        resetkeycode()
        
    elif loggedinmenu == '4':
        
        print("Logging you out...")
        print("")
        userafter()
    else:
        print("Invalid Input.")
        print("")
        loggedin()
        
def sendtofile():
    
    print("")
    print("No file added yet.")
    print("")
    print("Closing vault.")
    print("")
    
    loggedinname()
    
def passsection():

    while True:
    
        userinput=input("Key code? (Enter 'n' to cancel) ")
        
        if userinput == keycode:
            
            print("")
            print("Access Granted.")
            sendtofile()
            
        elif userinput == 'n':
            
            print("")
            print("Vault login stopped.")
            print("")
            
            loggedinname()
    
        else:
        
            print("")
            print("Access Denied OR Invalid Input.")
            print("")
        
def vaultstart():
    
    print("Secure pin locked file vault.")
    print("")
    
    passsection()
    
def resetpassword():
    
    print("Reset password.")
    resetcontinue=input("Are you sure you want to continue? (y/n) ")
    print("")
    
    if resetcontinue == 'y':
        resetpasswordcontinue()
    elif resetcontinue == 'n':
        loggedinname()
    else:
        print("Invalid Input. Try again...")
        print("")
        resetpassword()
        
def resetkeycode():
    
    print("Reset keycode.")
    resetcontinue=input("Are you sure you want to continue? (y/n) ")
    print("")
    
    if resetcontinue == 'y':
        resetkeycodecontinue()
    elif resetcontinue == 'n':
        loggedinname()
    else:
        print("Invalid Input. Try again...")
        print("")
        resetkeycode()
        
def resetpasswordcontinue():
    
    global passreal
    
    passcheck=input("New password: ")
    passchecktwo=input("Enter password again: ")
    
    if passcheck == passchecktwo:
        print("")
        
        passreal = passchecktwo
        
        print("Success!")
        print("")
        
        loggedinname()
        
    else:
        print("")
        print("Passwords don't match. Try again.")
        print("")
        
        resetpasswordcontinue()
    
def resetkeycodecontinue():

    global keycode
    
    keycodecheckpoint=input("Password to continue: (Enter 'n' to go back) ")
    
    if keycodecheckpoint == passreal:
        
        print("")
        
    elif keycodecheckpoint == 'n':
        
        print("")
        print("Reset stopped.")
        print("")
        loggedinname()
        
    else:
        
        print("")
        print("Wrong. Try again.")
        print("")
        resetkeycodecontinue()
    
    keycheck=input("New key code: ")
    keychecktwo=input("Enter key code again: ")
    
    if keycheck == keychecktwo:
        
        print("")
        
        keycode = keychecktwo
        
        print("Success!")
        print("")
        
        loggedinname()
        
    else:
        print("")
        print("Key codes don't match. Try again.")
        print("")
        
        resetkeycodecontinue()
    
user()
