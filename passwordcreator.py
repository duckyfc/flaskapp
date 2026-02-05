import random
badGuess = 0
loggedin = False
Letters = "qwertyuiopasdfghjklzxcvbnm"
BigL = "QWERTYUIOPASDFGHJKLZXCVBNM"
Nums = "1234567890"
Spec = ["!","@","$","%","^","&","*"]
Accounts = {}
key1 = False
key2 = False
key3 = False
key4 = False

def generate_password():
    password = ""
    Upper = 0
    Special = 0
    Number = 0
    Length = 0 
    for i in range(5):
        password += random.choice(Letters)
        Length += 1
    password += random.choice(BigL)
    Length += 1
    Upper += 1
    password += random.choice(Nums)
    Length += 1
    Number += 1
    password += random.choice(Spec)
    Length += 1
    Special += 1
    return password, Length, Upper, Special, Number

finalPassword, finalLength,finalUpper,finalSpecial,finalNumber = generate_password() 
def validpassword(finalLength, finalUpper, finalSpecial, finalNumber):
    if finalLength >= 8 and finalSpecial >= 1 and finalUpper >= 1 and finalNumber >= 1:
        return True
    else:
        return False



while 1+1 == 2:
    if badGuess < 3:

        while loggedin == True:
            print("Press: 1 -- My Profile | 2 -- Settings | 3 -- Log Out")

            nput = input() 

            if nput == "1":
                print("My Profile | Press 1 to exit")
                print ("Username: " + str(username))
                print ("Password: " + str(Accounts[username]))
                if input() == 1:
                    loggedin == True
                    








            if nput == "2":
                print("Settings | Press: 1 -- Exit | 2 -- Change Username | 3 -- Change Password")
                setput = input()


                if setput == "1":
                    loggedin == True


                if setput == "2":
                    print("Please enter your CURRENT USERNAME:")
                    olduser = input()
                    if olduser in Accounts:
                        

                        print("Please enter your PASSWORD:")
                        passwordguess = input()

                        if passwordguess == Accounts[olduser]:
                            print("Please input your new username")
                            username = input()
                            Accounts[username] = passwordguess
                            print("Username changed successfully!")
                            Accounts.pop(olduser)
                            loggedin = True
                            
                        else:
                            print("Your password is incorrect")
                            loggedin = True
                    else:
                        print("Your username is incorrect")
                        loggedin = True





                if setput == "3":
                    print("Please enter your USERNAME:")
                    if input() in Accounts:

                        print("Please enter your CURRENT PASSWORD:")
                        passwordguess = input()

                        if passwordguess == Accounts[username]:
                            print("Please input your NEW PASSWORD")
                            passwordAttempt = input()

                            for i in range(len(passwordAttempt)):
                                if len(passwordAttempt) >= 8:
                                    key1 = True
                                if passwordAttempt[i] in Spec:
                                    key2 = True
                                if passwordAttempt[i] in Nums:
                                    key3 = True 
                                if passwordAttempt[i] in BigL:
                                    key4 = True
                                

                            if key1 == True and key2 == True and key3 == True and key4 == True:
                                print("Password changed successfully!")
                                Accounts[username] = passwordAttempt
                                key1 = False
                                key2 = False
                                key3 = False
                                key4 = False
                            else:
                                print("Not a valid password!")
                                loggedin = True
                                key1 = False
                                key2 = False
                                key3 = False
                                key4 = False
                            
                        else:
                            print("Your password is incorrect")
                            loggedin = True
                    else:
                        print("Your username is incorrect")
                        loggedin = True










            if nput == "3":
                print("Successfully logged out!")
                loggedin = False

            
        print("Press: 1 -- Create an Account | 2 -- Log in")

        put = input()


        if put == "1":

            print("Please Create a USERNAME:")
            
            name = input()
            if name not in Accounts:
                username = name

                if username != "":
                    
                    generate_password()
                    
                    if validpassword(finalLength, finalUpper, finalSpecial, finalNumber) == True:

                        print("Your password is", finalPassword)



                print("Please re-enter your USERNAME:")

                if input() == username:

                    print("Please enter your PASSWORD:")
                    passwordguess = input()


                    if passwordguess == finalPassword:
                        print("You have successfully created an account!")

                        Accounts[username] = finalPassword

                    else:
                        print("Your password is incorrect")
                else:
                    print("Your username is incorrect")
            else: 
                print("Username already taken!")

        if put == "2":

            print("Please enter your USERNAME:")


            if input() in Accounts:
                print("Please enter your PASSWORD:")
                passwordguess = input()

                if passwordguess == Accounts[username]:
                    print("You have successfully logged in!")
                    loggedin = True
                else:
                    print("Your password is incorrect")
                    badGuess += 1

            else:
                print("Your username is incorrect")
                
   


    if badGuess == 3:
        print("Sorry, you have inputted the wrong password too many times. :(")
        print("You have to create an account now")
        print("Please Create a USERNAME:")
        
        name = input()
        if name not in Accounts:
            username = name

            if username != "":
                
                generate_password()
                
                if validpassword(finalLength, finalUpper, finalSpecial, finalNumber) == True:

                    print("Your password is", finalPassword)
                    print("Please re-enter your USERNAME:")

                if input() == username:

                    print("Please enter your PASSWORD:")
                    passwordguess = input()


                    if passwordguess == finalPassword:
                        print("You have successfully created an account!")

                        Accounts[username] = finalPassword
                        badGuess = 0 

                    else:
                        print("Your password is incorrect")
                else:
                    print("Your username is incorrect")
            else: 
                print("Username already taken!")