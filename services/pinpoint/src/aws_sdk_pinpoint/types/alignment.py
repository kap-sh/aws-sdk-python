"""Generated from Smithy shape ``com.amazonaws.pinpoint#Alignment``."""

from typing import Literal, TypeAlias, cast

Alignment: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Alignment) -> str:
    return value


def deserialize_json(data: str) -> Alignment:
    return cast(Alignment, data)
