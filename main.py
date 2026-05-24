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
7. Exit
=========================================
"""
    print(menu_text)

def get_user_choice() -> str:
    while True:
        choice = input("Please select an option (1-7): ")
        if choice not in ("1","2","3","4","5","6","7"):
            print("Your selection is invalid. Please select between (1-7)")
        else:
            return choice

def handle_add_soldier() -> None:
    while True:
        id = input("Enter the soldier id ")
        name = input("Enter the soldier name ")
        back_to_menu = input("Do you want to return to the menu (y/n)")
        if back_to_menu =="y":
            break
        try:
            add_soldier(id, name)
            print("The soldier was successfully added")
            break
        except ValueError as e:
            print(e)
            continue

def handle_remove_soldier() -> None:
        while True:
            id = input("Enter the soldier id ")
            back_to_menu = input("Do you want to return to the menu (y/n)")
            if back_to_menu =="y":
                break
            try:
                remove_soldier(id)
                print("The soldier was successfully removed")
                break
            except KeyError as e:
                print(e)
                continue

def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()
    if not soldiers:
        print("There are no soldiers in the system")
        return None
    for soldier in soldiers:
        print(f"ID: {soldier["id"]} | Name: {soldier["name"]}")
        print("Duties")
        if soldier["duties"]:
            for duty in soldier["duties"]:
                print(f"  - {duty['name']} (Status: {duty['status']})")
        else:
            print("No duties assigned")
        print("-" * 30)


def handle_add_duty() -> None:
    while True:
        id = input("Enter the soldier id ")
        name = input("Enter the duty name ")
        day = input("Enter the duty day ")
        back_to_menu = input("Do you want to return to the menu (y/n)")
        if back_to_menu =="y":
            break
        try:
            add_duty_to_soldier(id, name, day)
            print("The duty was successfully added")
            break
        except KeyError as e:
            print(e)
            continue
        except ValueError as e:
            print(e)
            continue
    

def handle_update_duty_status() -> None:
    while True:
        id = input("Enter the soldier id ")
        name = input("Enter the duty name ")
        status = input("Enter the new status ")
        back_to_menu = input("Do you want to return to the menu (y/n)")
        if back_to_menu =="y":
            break
        try:
            update_duty_status(id, name, status)
            print("The duty was successfully updated")
            break
        except KeyError as e:
            print(e)
            continue
        except ValueError as e:
            print(e)
            continue

def handle_view_soldier_duties() -> None:
    while True:
        id = input("Enter the soldier id ")
        back_to_menu = input("Do you want to return to the menu (y/n)")
        if back_to_menu =="y":
            break
        try:
            duties = get_soldier_duties(id)
            if not duties:
                print("No duties assigned")
                break
            for duty in duties:
               print(f"  - {duty['name']} on {duty['day']} (Status: {duty['status']})")
            break
        except KeyError as e:
            print(e)
            continue


def main() -> None:
    menu_choices={"1": handle_add_soldier, 
                  "2": handle_remove_soldier, 
                  "3": handle_view_soldiers, 
                  "4": handle_add_duty, 
                  "5": handle_update_duty_status, 
                  "6": handle_view_soldier_duties,
                  "7": exit}
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == "7":
            print("Good day and goodbye")
        menu_choices[choice]()

if __name__ =="__main__":
    main()
