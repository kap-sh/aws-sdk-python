"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MotionImagePlayback``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify whether your motion graphic overlay repeats on a loop or plays only once."""
MotionImagePlayback: TypeAlias = Literal[
    "ONCE",
    "REPEAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONCE",
        "REPEAT",
    )
)


def serialize_json(value: MotionImagePlayback) -> str:
    return value


def deserialize_json(data: str) -> MotionImagePlayback:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MotionImagePlayback value: {data!r}")
    return cast(MotionImagePlayback, data)
