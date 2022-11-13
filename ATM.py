import pandas as pd


class AtmMachine:
    def __init__(self, database):
        self.database = database
        self.df = pd.read_csv(database)
        self.index = -1

    def create_account(self, name, amount, pin):
        new_account_number = self.df['Account Number'].max() + 1
        data = [[new_account_number, name, amount, pin]]
        new_account = pd.DataFrame(data, columns=self.df.columns)
        self.index = len(self.df)

        new_account.to_csv(self.database, mode='a', header=False, index=False)
        self.df = pd.read_csv(self.database)
        return new_account_number

    def withdraw(self, amount):

        if self.df.iloc[self.index][2] < int(amount):
            return 'Insufficient funds'
        else:
            self.df.iat[self.index, 2] = self.df.iloc[self.index][2] - int(amount)
            self.df.to_csv(self.database, index=False)
            return 'successful!'

    def deposit(self, amount):

        self.df.iat[self.index, 2] = self.df.iloc[self.index][2] + int(amount)
        self.df.to_csv(self.database, index=False)
        return 'successful!'

    def change_pin(self, account_number, pin, new_pin):
        index = self.df[self.df['Account Number'] == int(account_number)].index.values.astype(int)[0]

        if self.df.iloc[index][3] != int(pin):
            return 'wrong pin'

        self.df.iat[index, 3] = int(new_pin)
        self.df.to_csv(self.database, index=False)
        return 'successful!'

    def check_details(self, account_number, pin):

        return f"""
        Account Name: {self.df.iloc[self.index][1]}
        Account Number: {self.df.iloc[self.index][0]}
        Balance: {self.df.iloc[self.index][2]}
        
        """

    def check_account(self, account_number):

        try:
            self.index = self.df[self.df['Account Number'] == int(account_number)].index.values.astype(int)[0]
        except AttributeError:
            return 'Invalid Account Number!'
        except IndexError:
            return 'Invalid Account Number!'
        return self.df.iloc[self.index][1]

    def login(self, pin):

        if self.df.iloc[self.index][3] != int(pin):
            return 'Wrong pin!'
        else:
            return 'successful!'
