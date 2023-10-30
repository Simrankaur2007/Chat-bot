from typing import Union

# Constants
ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = ["balance", "deposit", "exit"]

# Helper Functions
def get_account() -> int:
    """
    Prompt the user for the account number and return it as an integer.
    """
    while True:
        try:
            account = int(input("Please enter your account number: "))
            if account not in ACCOUNTS:
                print("Account number does not exist. Please try again.")
            else:
                return account
        except ValueError:
            print("Account number must be a whole number.")



def get_amount() -> float:
    """
    Prompt the user for the amount to deposit and return it as a float.
    """
    while True:
        try:
            amount = float(input("Enter the transaction amount: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Amount must be numeric.")


def get_balance(account: int) -> str:
    """
    Retrieve the balance of a specified account.
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f'Your current balance for account {account} is ${balance:.2f}.'

def make_deposit(account: int, amount: float) -> str:
    """
    Update the balance of the specified account by adding the value of the amount.
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    ACCOUNTS[account]["balance"] += amount
    return f'You have made a deposit of ${amount:.2f} to account {account}.'

def user_selection() -> str:
    """
    Prompt the user for their selection and return it if valid.
    """
    while True:
        selection = input("What would you like to do (balance/deposit/exit)? ").strip().lower()
        if selection in VALID_TASKS:
            return selection
        else:
            print("Invalid task. Please choose balance, deposit, or exit.")

def chatbot():
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")

    while True:
        selection = user_selection()

        if selection == "balance":
            account = get_account()
            print(get_balance(account))
        elif selection == "deposit":
            account = get_account()
            amount = get_amount()
            print(make_deposit(account, amount))
        elif selection == "exit":
            print("Thank you for banking with PiXELL River Financial.")
            break

if __name__ == "__main__":
    chatbot()
