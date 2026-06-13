"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectProfileList``."""

from typing import TypeAlias

ProjectProfileList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectProfileList) -> list:
    return list(value)


def deserialize_json(data: list) -> ProjectProfileList:
    return list(data)
