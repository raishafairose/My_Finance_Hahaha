name = input("Enter your name : ")
print("Hello " + name.capitalize() +".")
balance = int(input("What is account balance right now? : "))
print("Press '1' if you want to do deposit ")
print("Press '2' if you want to withdraw : ")
choice = input("Enter here : ")


def value():
    if choice == "1":
        dp = int(input("How much you want to deposit : "))
        print("Amount deposit successful! ")
        print(f"Your current balance is {balance + dp}/- tk")
    elif choice == "2":
        wt = int(input("How much you want to withdraw : "))
        if wt > balance :
            print("Dear user, You don't have sufficient balance. ")
            print("Your current balance is " + str(balance) + "/- tk. ")
        else:
            print("Amount withdraw successful! ")
            print(f"Your current balance is {balance - wt}/- tk.")


    else :
        print("Dear user. Your amount is invalid. Put your value in digits. Thank you.")

    return
value()




