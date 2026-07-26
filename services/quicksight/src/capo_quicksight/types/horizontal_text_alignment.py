"""Generated from Smithy shape ``com.amazonaws.quicksight#HorizontalTextAlignment``."""

from typing import Literal, TypeAlias, cast

HorizontalTextAlignment: TypeAlias = Literal[
    "LEFT",
    "CENTER",
    "RIGHT",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: HorizontalTextAlignment) -> str:
    return value


def deserialize_json(data: str) -> HorizontalTextAlignment:
    return cast(HorizontalTextAlignment, data)
