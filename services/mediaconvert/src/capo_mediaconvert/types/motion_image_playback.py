"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImagePlayback``."""

from typing import Literal, TypeAlias, cast

"""Specify whether your motion graphic overlay repeats on a loop or plays only once."""
MotionImagePlayback: TypeAlias = Literal[
    "ONCE",
    "REPEAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MotionImagePlayback) -> str:
    return value


def deserialize_json(data: str) -> MotionImagePlayback:
    return cast(MotionImagePlayback, data)
