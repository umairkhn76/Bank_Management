class Bank:
    Bankname="Punjab National Bank"
    def __init__(self,accno,balance,pin):
        self.accno=accno
        self.balance=balance
        self.pin=pin
        print("Your Acc no is ",self.accno)
        print("Your Available balance",self.balance)

    def credit(self):
        self.balance=self.balance+self.amount
        print(f"Your acc has {self.amount} Rs/- credited")

    def debit(self):
        self.balance=self.balance-self.amount
        print(f"Your acc has {self.amount} Rs/- debited")

    def show(self):
        return self.balance


obj=Bank(8793450,1000,1234)
print(obj.Bankname)
obj.pin=int(input("Enter your pin: "))
if obj.pin==1234:
    user=input("Enter (Credit/Debit): ").capitalize()
    if user=="Credit":
        obj.amount=int(input("Enter amount you want to add : "))
        obj.credit()

    elif user=="Debit":
        print("Welcome to PNB")
        obj.amount=int(input("Enter amount you want to debited : "))
        obj.debit()
else:
    print("Wrong pin try later")

print("Your available balance",obj.show())

