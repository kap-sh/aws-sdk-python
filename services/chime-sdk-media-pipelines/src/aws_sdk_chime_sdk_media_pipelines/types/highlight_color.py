"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#HighlightColor``."""

from typing import Literal, TypeAlias, cast

HighlightColor: TypeAlias = Literal[
    "Black",
    "Blue",
    "Red",
    "Green",
    "White",
    "Yellow",
]


# --- restJson1 ser/de ---
def serialize_json(value: HighlightColor) -> str:
    return value


def deserialize_json(data: str) -> HighlightColor:
    return cast(HighlightColor, data)
