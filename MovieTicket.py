class Bank:
    b_name='SBI'
    branch='Nandigam'
    IFSC_code='SBIN0016958'

    def __init__(self,ac_holder,ac_no,age,pin):
        self.ac_holder=ac_holder
        self.ac_no=ac_no
        self.age=age
        self.pin=pin
        self.balance=1000

    def pin_check(self):
        pin=int(input('Enter Your Pin:'))
        return pin==self.pin

    def __str__(self):
        return f'{self.ac_holder}->{self.ac_no}'
    
    @classmethod
    def add_branch_manager(cls,manager):
        cls.manager=manager
    
    def holder_details(self):
        print('--------User Info--------')
        if self.pin_check():
            return f'''Welcome to {Bank.b_name} Bank.. Hello {self.ac_holder} with accno of {self.ac_no}
and a balance of {self.balance}. For the investment of ur amount u will get {self.invest_details()}
for the balance of {self.balance} Thank You.....'''
        print('Enter the valid pin')
        return self.holder_details()
    
    def deposit(self,amount):
        print('----Deposit Amount----')
        if self.pin_check():
            if amount>0:
                self.balance+=amount
                return f'''Amount deposited to accno {self.ac_no} with deposit amount of {amount}
and current balance is {self.balance}''' 
            else:
                return 'Enter Valid deposit amount (>0)'
        else:
            print('Invlaid Pin')
            return self.deposit()
        
    def withdrawal(self,amount):
        print('------Withdraw Amount-------')
        if self.pin_check():
            if 0 < amount <= self.balance:
                self.balance -= amount
                return True  
            else:
                print('Insufficient Balance ')
                return False
        print('Invalid Pin ')
        return False
    
    def bal_check(self):
        print('------Balance Check-------')
        if self.pin_check():
            return 'the current balance is {self.balance}'
        else:
            return self.bal_check()
        
    def ch_pin(self):
        print('------Change pin-------')
        if self.pin_check():
            new_pin=int(input('Enter new pin:'))
            self.pin=new_pin
        else:
            print('Invalid user')
            return self.ch_pin()
        
    @staticmethod
    def interest(amount,time=1,roi=12):
        return (amount*time*roi)/100
    
    def invest_details(self):
        print('------Invest Details-----') 
        if self.pin_check():
            pamount=self.balance
            return self.interest(pamount)

cus1=Bank('Gowtham Jami','20448771736',23,2025)
# print(cus1)
# print(cus1.holder_details())
# print(cus1.deposit())
# print(cus1.withdrawal())
# print(cus1.bal_check())
# print(cus1.holder_details())
# cus1.ch_pin()
# print(cus1.holder_details())
# cus1.add_branch_manager('Uma')
# print(Bank.manager)

class Movie:
    def __init__(self,screen_no,movie_name,time,available_tickets,price):
        self.screen_no=screen_no
        self.movie_name=movie_name
        self.time=time
        self.available_tickets=available_tickets
        self.price=price

    def __str__(self):
        return f'''Ur Checking for {self.movie_name} Movie
        In the Screen:{self.screen_no}
        And the time for {self.time}
        and the available tickets are {self.available_tickets} and each ticket costs {self.price}'''
    
    def book_tickets(self):
        no_of_tickets=int(input('Enter no.of Tickets:'))
        if 1<=no_of_tickets<=5:
            if no_of_tickets<=self.available_tickets:
                total=no_of_tickets*self.price
                print(f'Amount is {total}')
                print('Booking Now')
                # return self.book_now()
                if cus1.withdrawal(total):
                    self.available_tickets-=no_of_tickets
                    return f'''Booking Completed
                    Movie:{self.movie_name}
                    Tickets Booked:{no_of_tickets}
                    Amount Deducted: {total}    
                    Remaining Balance: {cus1.balance}'''
                else:
                    print('Payment Failed....')
                    return self.book_tickets()
            else:
                print(f"Sorry, there are only {self.available_tickets} left.")
                return self.book_tickets()
        else:
            print('Please Enter btw 1 - 5 Tickets')
            return self.book_tickets()


    # def book_now(self):
    #     if Bank.pin_check()==cus1.pin:
            


    
m1=Movie('screen1','Coolie','10:30 AM',200,250)
print(m1)
print(m1.book_tickets())
# print(cus1.balance)

