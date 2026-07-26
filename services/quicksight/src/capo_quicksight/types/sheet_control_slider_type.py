"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlSliderType``."""

from typing import Literal, TypeAlias, cast

SheetControlSliderType: TypeAlias = Literal[
    "SINGLE_POINT",
    "RANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlSliderType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlSliderType:
    return cast(SheetControlSliderType, data)
