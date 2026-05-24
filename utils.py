from data import soldiers


def find_soldier_by_id(soldier_id: int) -> dict | None:

    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            return soldier
    return None


