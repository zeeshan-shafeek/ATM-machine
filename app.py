import pandas as pd
from ATM import AtmMachine
import os
from getpass import getpass

#
# header = ['Name', 'M1 Score', 'M2 Score']
# data = [['Alex1', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
# data = pd.DataFrame(data, columns=header)
#
# data.to_csv('Stu_data.csv', mode='a', header=False, index=False)


# df = pd.read_csv('Stu_data.csv')
#
# # print(df)
#
# dfb = pd.DataFrame(columns=df.columns)
#
# print(df.iloc[1][2])

# dfb = df[df['Name'] == 'Joey'].index.values.astype(int)[0]
# # print(data.Name.where(data['M1 Score'] == 62))
# print(df)2

atm = AtmMachine('Database.csv')
pin = 0
account_no = 0
response = 0
amount = 0
name = ''
result = ''

while 1:
    os.system("cls")
    print("*****Welcome!*****")
    print("1. Create Account")
    response = int(input("2. Access Account \n"))
    if response == 2:
        account_no = input("Account Number: ")
        name = atm.check_account(account_no)
        if name != 'Invalid Account Number!':
            pin: str = getpass('Pin: ')
            # pin = input("Pin: ")
            result = atm.login(pin)
            print(result)
            if result == 'successful!':
                break
            else:
                input("press enter to try again")
        else:
            print(name)
            input("press enter to try again")

    elif response == 1:
        name = input("please enter your name: ")
        # pin = input("enter pin: ")
        pin: str = getpass('Pin: ')
        amount = input("enter amount: ")
        account_no = atm.create_account(name, amount, pin)
        print(f" Your Account number is: {account_no}")
        input("press enter to continue")
        break
    else:
        print("invalid input")

option = 0

while option != 5:

    os.system("cls")
    print(f"""
Name:{name}    Account no.{account_no}
*********************
    Menu:
    1. Account Detail
    2. Change Pin
    3. Deposit
    4. Withdraw
    5. Exit
*********************
            """)

    option = int(input("Enter 1, 2, 3, 4 or 5: "))

    if option == 1:

        print(atm.check_details(account_no, pin))
        input("press enter to continue")
        continue
    elif option == 2:
        while 1:
            pin: str = getpass('please re-enter pin: ')
            # pin = input("please re-enter pin: ")
            new_pin: str = getpass('please enter new pin: ')
            # new_pin = input("please enter new pin: ")
            result = atm.change_pin(account_no, pin, new_pin)
            print(result)
            input("press enter to continue")
            if result != 'wrong pin':
                break

    elif option == 3:
        amount = input("enter Amount: ")
        print(atm.deposit(amount))
        input("Press enter to continue")
    elif option == 4:
        amount = input("enter Amount: ")
        print(atm.withdraw(amount))
        input("Press enter to continue")
    elif option == 5:
        break
    else:
        print("invalid response")
