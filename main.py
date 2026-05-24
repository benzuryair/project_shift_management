from soldier_manager import *
from duty_manager import *

def show_menu() -> None:
    menu_text = """
=========================================
        SHIFT MANAGEMENT SYSTEM
=========================================
1. Add a new soldier
2. Remove a soldier
3. View all soldiers
4. Add a duty to a soldier
5. Update duty status
6. View duties of a specific soldier
=========================================
"""
    print(menu_text)

def get_user_choice() -> str:
    while True:
        choice = input("Please select an option (1-6): ")
        if choice not in ("1","2","3","4","5","6"):
            print("Your selection is invalid. Please select between (1-6)")
        else:
            return choice

def handle_add_soldier() -> None:
    while True:
        id = input("Enter the soldier id ")
        name = input("Enter the soldier name ")
        try:
            add_soldier(id, name)
            print("The soldier was successfully added")
            break
        except ValueError as e:
            print(e)
            continue
        