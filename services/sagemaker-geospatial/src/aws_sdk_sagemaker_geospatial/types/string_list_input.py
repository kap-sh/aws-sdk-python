"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StringListInput``."""

from typing import TypeAlias

StringListInput: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StringListInput) -> list:
    return list(value)


def deserialize_json(data: list) -> StringListInput:
    return list(data)
