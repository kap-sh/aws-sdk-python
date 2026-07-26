"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#BorderColor``."""

from typing import Literal, TypeAlias, cast

BorderColor: TypeAlias = Literal[
    "Black",
    "Blue",
    "Red",
    "Green",
    "White",
    "Yellow",
]


# --- restJson1 ser/de ---
def serialize_json(value: BorderColor) -> str:
    return value


def deserialize_json(data: str) -> BorderColor:
    return cast(BorderColor, data)
