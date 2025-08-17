class MinimumBalanceError(Exception):
    """Custom exception for when balance falls below minimum."""
    pass

class DepositLimitError(Exception):
    """Custom exception when deposit cap is exceeded."""
    pass

class InsufficientFundsError(Exception):
    """Custom exception when withdrawal is more than balance."""
    pass


def banking_app():
    balance = 300
    total_deposited = 0
    MIN_BALANCE = 100
    DEPOSIT_CAP = 3000

    print("Welcome to your Banking App!")
    print(f"Your starting balance is: ${balance:.2f}\n")

    while True:
        try:
            action = input("Would you like to withdraw (w), deposit (d), or quit (q)? ").lower()

            if action == 'q':
                print("Thank you for using the Banking App. Goodbye!")
                break

            elif action == 'w':
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    raise InsufficientFundsError("Insufficient funds.")
                balance -= amount
                print(f"Withdrawal successful. Current balance: ${balance:.2f}")

                if balance <= MIN_BALANCE:
                    raise MinimumBalanceError("ATTENTION: The account is below minimum daily balance!")

            elif action == 'd':
                amount = float(input("Enter amount to deposit: "))
                if total_deposited + amount > DEPOSIT_CAP:
                    raise DepositLimitError("Deposit cap of $3000 exceeded. Cannot add more.")
                balance += amount
                total_deposited += amount
                print(f"Deposit successful. Current balance: ${balance:.2f}")

            else:
                print("Invalid option. Please enter w, d, or q.")

        except InsufficientFundsError as ife:
            print(ife)
        except MinimumBalanceError as mbe:
            print(mbe)
        except DepositLimitError as dle:
            print(dle)
        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    banking_app()