class Bank_Account:
    def __init__(self,acc_name,acc_number,acc_balance):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.acc_balance=acc_balance
    def deposit(self,amount_deposited,):
        Total_balance=amount_deposited + self.acc_balance
        return Total_balance
    def withdrawal(self,amount_withdrawn):
        Balance_after_withdrawal=self.acc_balance - amount_withdrawn
        return Balance_after_withdrawal
    def check_balance(self):
        return self.acc_balance
Acc_owner_1=Bank_Account("Tobi Olude","0034265895",15000)
print(Acc_owner_1.acc_name)
print( "My acc balance is: " + " "+ str (Acc_owner_1.withdrawal(10000)))
print(Acc_owner_1.check_balance())