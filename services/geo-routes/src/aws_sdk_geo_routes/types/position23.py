"""Generated from Smithy shape ``com.amazonaws.georoutes#Position23``."""

from typing import TypeAlias

Position23: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: Position23) -> list:
    return list(value)


def deserialize_json(data: list) -> Position23:
    return list(data)
