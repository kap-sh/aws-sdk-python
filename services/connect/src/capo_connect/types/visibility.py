"""Generated from Smithy shape ``com.amazonaws.connect#Visibility``."""

from typing import Literal, TypeAlias, cast

Visibility: TypeAlias = Literal[
    "ALL",
    "ASSIGNED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Visibility) -> str:
    return value


def deserialize_json(data: str) -> Visibility:
    return cast(Visibility, data)
