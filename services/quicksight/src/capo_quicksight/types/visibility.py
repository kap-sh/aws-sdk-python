"""Generated from Smithy shape ``com.amazonaws.quicksight#Visibility``."""

from typing import Literal, TypeAlias, cast

Visibility: TypeAlias = Literal[
    "HIDDEN",
    "VISIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Visibility) -> str:
    return value


def deserialize_json(data: str) -> Visibility:
    return cast(Visibility, data)
