"""Generated from Smithy shape ``com.amazonaws.location#Position``."""

from typing import TypeAlias

Position: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Position) -> list:
    return list(value)


def deserialize_json(data: list) -> Position:
    return list(data)
