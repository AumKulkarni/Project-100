class atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def know_balance(self):
        print("Your balance is 20000")
    def cash_withdraw(self,amount):
        new_balance=20000-amount
        print("You have withdrawn"+str(amount)+"and your remaining balance is"+str(new_balance))
def main():
    card_number=input("enter your card number")
    pin_number=input("enter your pin")
    new_user=atm(card_number,pin_number)
    print("choose the option")
    print("1 know your balance 2 withdraw")
    activity=int(input("enter your option"))
    if (activity==1):
        new_user.know_balance()
    elif (activity==2):
        amount=int(input("enter the withdrawl amount"))
        new_user.cash_withdraw(amount)
    else:
        print("please enter a valid number")
if __name__=="__main__":
    main()


