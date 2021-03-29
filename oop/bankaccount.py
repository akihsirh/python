# A class with class variables, instance variables, class methods and instance methods
class BankAccount:
    """
    A bank account class that specifies the owner and balance of the account.
    """

    active_accounts = 0
    bank_name = "Python Bank"

    @classmethod
    def display_active_accounts(cls):
        """
        Prints the number of active account in the bank.
        """
        print(f"Number of active accounts: {cls.active_accounts}")

    @classmethod
    def validate_info(cls, acct_info):
        """
        This function validates the account info passed via a string
        Args:
            acct_info (): A list containing account owner and balance info
        """
        if len(acct_info) != 2:
            raise ValueError("Passed more than two parameter. Need only owner and balance.")
        elif len(acct_info[0]) < 1:
            raise ValueError("Invalid owner name.")
        elif not acct_info[1].isnumeric:
            raise ValueError("Invalid account balance.")

    @classmethod
    def from_string(cls, acct_str):
        """
        Creates a new instance of the user class using account information passed via user input string.
        Args:
            acct_str (): User input string specifying account owner and starting balance.
        """
        acct_info = acct_str.split(",")
        cls.validate_info(acct_info)
        owner, balance = acct_info[0], int(acct_info[1])
        return cls(owner, balance)

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        BankAccount.active_accounts += 1

    def get_owner(self):
        """
        Returns:
            Current account owner name.
        """
        return self.owner

    def get_balance(self):
        """
        Returns:
            Current account balance in dollars.
        """
        return self.balance

    def deposit(self, deposit):
        """

        Args:
            deposit (): Adds user deposit (in dollars) to account balance.

        Returns:
            The updated balance.
        """
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        """

        Args:
            withdraw (): Subtracts user withdrawal amount (in dollars) from account balance.

        Returns:
            The updated balance.
        """
        self.balance -= withdraw
        return self.balance

    def close_account(self):
        """
        Empties the balance of the account and reduces the number of customers in the bank
        Returns:
            A message saying that the account owner has closed the account.
        """
        self.balance = 0
        BankAccount.active_accounts -= 1
        return f"{self.owner} has closed the account. Account balance has been set to {self.balance}"

# Create bank account
acct = BankAccount("Mochi", 10000)
print(f"New account created by {acct.get_owner()}")
deposit_amt = 5000
acct.deposit(deposit_amt)
print(f"Balance after {deposit_amt} dollar deposit: {acct.get_balance()}")
withdraw_amt = 1000
acct.withdraw(withdraw_amt)
print(f"Balance after {withdraw_amt} dollar withdrawal: {acct.get_balance()}")

# Create bank account
acct2 = BankAccount("Ramen", 2000)
print(f"New account created by {acct2.get_owner()}")

BankAccount.display_active_accounts()
print(acct2.close_account())
BankAccount.display_active_accounts()

# Create a bank account from a string
acct3 = BankAccount.from_string("Bingsoo,9000")
print(f"New account created by {acct3.get_owner()}")
BankAccount.display_active_accounts()

# Just looking at ids
print(id(acct.bank_name))
print(id(acct3.bank_name))
print(id(BankAccount.bank_name))