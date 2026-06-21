"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageScalingType``."""

from typing import Literal, TypeAlias, cast

SheetImageScalingType: TypeAlias = Literal[
    "SCALE_TO_WIDTH",
    "SCALE_TO_HEIGHT",
    "SCALE_TO_CONTAINER",
    "SCALE_NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageScalingType) -> str:
    return value


def deserialize_json(data: str) -> SheetImageScalingType:
    return cast(SheetImageScalingType, data)
