"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorFillType``."""

from typing import Literal, TypeAlias, cast

ColorFillType: TypeAlias = Literal[
    "DISCRETE",
    "GRADIENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ColorFillType) -> str:
    return value


def deserialize_json(data: str) -> ColorFillType:
    return cast(ColorFillType, data)
