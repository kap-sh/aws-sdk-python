"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#NumValues``."""

from typing import TypeAlias

NumValues: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: NumValues) -> list:
    return list(value)


def deserialize_json(data: list) -> NumValues:
    return list(data)
