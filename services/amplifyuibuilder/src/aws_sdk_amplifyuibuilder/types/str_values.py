"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StrValues``."""

from typing import TypeAlias

StrValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StrValues) -> list:
    return list(value)


def deserialize_json(data: list) -> StrValues:
    return list(data)
