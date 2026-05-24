from data import soldiers


def find_soldier_by_id(soldier_id: int) -> dict | None:

    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            return soldier
    return None


def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty["name"] == duty_name:
            return duty
    return None


def is_valid_status(status: str) -> bool:
    return status in ("pending", "completed", "missed")


def is_valid_name(name: str) -> bool:
    return name .strip() != ""


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    return duty_name in [duty["name"] for duty in soldier["duties"]]
