"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ActionList``."""

from typing import TypeAlias

ActionList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    return list(value)


def deserialize_json(data: list) -> ActionList:
    return list(data)
