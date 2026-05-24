from utils import *
from data import soldiers

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier is None:
        raise KeyError("The soldier does not exist in the system!")
    if soldier_has_duty(soldier,duty_name):
        raise ValueError("This duty already exists for the soldier!")
    if not is_valid_day(day):
        raise ValueError("The day entered is invalid. Enter between Sunday and Thursday!")
    soldier["duties"].append({"name": duty_name, "day":day, "status": "pending"})


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier == None:
        raise KeyError("The soldier does not exist in the system!")
    duty=find_duty_by_name(soldier["duties"],duty_name)
    if duty == None:
        raise KeyError("This duty does not exist for the soldier!")
    if not is_valid_status(new_status):
        raise ValueError("The duty status is incorrect!")
    duty["status"] = new_status
