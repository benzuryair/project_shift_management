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
