import os
import time

credentials = [
    {"username": "admin", "password": "admin"},
]

logs = []

# Initialize balance
balance = 100000

def make_payment(amount, username):
    global balance
    if balance >= amount:
        balance -= amount
        print(f"Payment of ₱{amount} successful!")
        # Log payment transaction
        log_activity(username, "Payment", f"Amount: ₱{amount}, Balance: ₱{balance}")
        return True
    else:
        print("Insufficient funds. Please add more funds.")
        return False


def view_logs():
    print("Log Activities:")
    for log in logs:
        print(log)
    input("Press Enter to return to the main menu...")

def log_activity(username, activity, details=""):
    logs.append(f"{username}: {activity} - {details}")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def before_lg():
    clear_console()
    print("1. Login")
    print("2. Register")
    print("3. Exit")

def menu_lg():
    print("|=========================================|")
    print("|              MEKUS-MEKUS                |")
    print("|           CAR RENTAL SYSTEM             |")
    print("|=========================================|")
    print()

    before_lg()
    while True:
        try:
            lg_choice = input("Enter your choice 1 - 3:  ")

            if lg_choice == "1":
                time.sleep(1)
                main_lg()
            elif lg_choice == "2":
                register()
            elif lg_choice == "3":
                time.sleep(2)
                before_lg()
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def register():
    clear_console()
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    new_number = input("Enter your number: ")
    new_id = input("Enter your valid id: ")
    credentials.append({"username": new_username, "password": new_password})
    print("Registration successful!")
    time.sleep(1)
    before_lg()

def main_lg():
    clear_console()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        matching_credentials = [
            cred for cred in credentials
            if cred["username"] == username and cred["password"] == password
        ]
        if matching_credentials:
            print("Welcome User", username)
            log_activity(username, "logged in")
            main_menu(username)
            break
        else:
            print("Invalid username or password. Try again.")

def main_menu(username):
    print("Choose an option:")
    print("1. View cars")
    print("2. View Logs")
    print("3. Logout")

    while True:
        try:
            main_menu_choice = input("Enter your choice 1 - 3: ")

            if main_menu_choice == "1":
                view_cars(username)
            elif main_menu_choice == "2":
                view_logs()
            elif main_menu_choice == "3":
                before_lg()
                break
            else:
                print("Invalid input, select choice from 1 - 3.")
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def view_cars(username):
    clear_console()
    print("Choose an option:")
    print("1. Available cars")
    print("2. Request car")
    print("3. Back")
    while True:
        try:
            view_choice = input("Enter your choice 1 - 3: ")

            if view_choice == "1":
                display_available_cars(username)
            elif view_choice == "2":
                request_car(username)
            elif view_choice == "3":
                main_menu(username)
                break
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def display_available_cars(username):
    clear_console()
    print("""
    Car rate:   
        ₱2,000/day
        ₱5,000/3 days
        ₱12,000/7 days
    """)
    print("Available cars")
    print("1. brand: Toyota", "model: Camry")
    print("2. brand: Honda", "model: Accord")
    print("3. brand: Ford", "model: Mustang")
    print("4. Cancel")
    while True:
        try:
            dpl_choice = input("Please pick your preferred car 1 - 4: ")

            if dpl_choice in ["1", "2", "3"]:
                color_available_cars(username)
            elif dpl_choice == "4":
                main_menu(username)
                break
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def color_available_cars(username):
    clear_console()
    print("Available colors")
    print("1. Red")
    print("2. Blue")
    print("3. Green")
    print("4. Cancel")
    while True:
        try:
            clr_choice = input("Enter your choice 1 - 4: ")

            if clr_choice in ["1", "2", "3"]:
                _policy(username)
            elif clr_choice == "4":
                main_menu(username)
                break
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def _policy(username):
    clear_console()
    print("""
    After confirming the transaction, the user is required to return the car earlier  
            than initially scheduled. Failure to adhere to this condition will 
                result in the user being subject to the established policy.
    """)
    print("Choose rental duration:")
    print("1. 1 day - ₱2,000")
    print("2. 3 days - ₱5,000")
    print("3. 7 days - ₱12,000")
    print("4. Cancel")

    while True:
        try:
            policy_choice = input("Select choice 1 - 4: ")

            if policy_choice == "1":
                amount = 2000
                print("You have rented a car for 1 day. Payment: ₱2,000")
                payment(amount, username)  # Pass username here
                details = "Confirmed rental for 1 day"
                log_activity(username, "Rented a car", details)
                main_menu(username)
                break
            elif policy_choice == "2":
                amount = 5000
                print("You have rented a car for 3 days. Payment: ₱5,000")
                payment(amount, username)  # Pass username here
                details = "Confirmed rental for 3 days"
                log_activity(username, "Rented a car", details)
                main_menu(username)
                break
            elif policy_choice == "3":
                amount = 12000
                print("You have rented a car for 7 days. Payment: ₱12,000")
                payment(amount, username)  # Pass username here
                details = "Confirmed rental for 7 days"
                log_activity(username, "Rented a car", details)
                main_menu(username)
                break
            elif policy_choice == "4":
                main_menu(username)
                break
            else:
                print("Invalid Input, Please Enter a number.")
        except ValueError:
            print("Invalid Input, Please Enter a number.")



def request_car(username):
    clear_console()
    print("""
    If you want a special car with extra features like leather seats or GPS, you'll need to 
        pay a bit more. The cost depends on the extras you choose. After you decide, the 
            total price for renting the car, including these add-ons, will be shown 
                to you. You'll see these costs before finalizing your rental.
    """)
    print("1. Confirmed")
    print("2. Cancel")
    while True:
        try:
            request_choice = input("Select choice 1 - 2: ")

            if request_choice == "1":
                print("You've requested a car successfully. You can now claim the car within 3 days.")
                details = "Confirmed car request"
                log_activity(username, "Requested a car", details)
                main_menu(username)
                break
            elif request_choice == "2":
                main_menu(username)
                break
        except ValueError:
            print("Invalid Input, Please Enter a number.")

def payment(amount, username):
    global balance
    while True:
        print("\npayment method....")
        print(f"Current balance: ₱{balance}")
        print(f"Total Payment: ₱{amount}")
        print("1. Make Payment")
        print("2. Cancel")

        choice = input("Enter your choice: ")

        if choice == '1':
            if make_payment(amount, username):  # Pass username here
                break
            else:
                print("Payment failed. Please try again.")
        elif choice == '2':
            _policy(username)
            break
        else:
            print("Invalid choice. Please try again.")



main_lg()
