"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImageInsertionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Choose the type of motion graphic asset that you are providing for your overlay. You can choose either a .mov file or a series of .png files."""
MotionImageInsertionMode: TypeAlias = Literal[
    "MOV",
    "PNG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MOV",
        "PNG",
    )
)


def serialize_json(value: MotionImageInsertionMode) -> str:
    return value


def deserialize_json(data: str) -> MotionImageInsertionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MotionImageInsertionMode value: {data!r}")
    return cast(MotionImageInsertionMode, data)
