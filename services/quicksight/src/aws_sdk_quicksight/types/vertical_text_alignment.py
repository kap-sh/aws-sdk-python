"""Generated from Smithy shape ``com.amazonaws.quicksight#VerticalTextAlignment``."""

from typing import Literal, TypeAlias, cast

VerticalTextAlignment: TypeAlias = Literal[
    "TOP",
    "MIDDLE",
    "BOTTOM",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: VerticalTextAlignment) -> str:
    return value


def deserialize_json(data: str) -> VerticalTextAlignment:
    return cast(VerticalTextAlignment, data)
