from utils import *
from data import soldiers


def add_soldier(soldier_id: int, name: str) -> None:
    if find_soldier_by_id(soldier_id) is not None:
        raise ValueError("There is a soldier with this ID!")
    if not is_valid_name(name):
        raise ValueError("The name is not valid")
    soldiers.append({"id": soldier_id, "name": name, "duties": []})
  