"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImageInsertionMode``."""

from typing import Literal, TypeAlias, cast

"""Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files."""
MotionImageInsertionMode: TypeAlias = Literal[
    "MOV",
    "PNG",
]


# --- restJson1 ser/de ---
def serialize_json(value: MotionImageInsertionMode) -> str:
    return value


def deserialize_json(data: str) -> MotionImageInsertionMode:
    return cast(MotionImageInsertionMode, data)
