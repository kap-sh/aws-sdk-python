"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninPosition``."""

from typing import Literal, TypeAlias, cast

"""Timecode Burnin Position"""
TimecodeBurninPosition: TypeAlias = Literal[
    "BOTTOM_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
    "MIDDLE_CENTER",
    "MIDDLE_LEFT",
    "MIDDLE_RIGHT",
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurninPosition) -> str:
    return value


def deserialize_json(data: str) -> TimecodeBurninPosition:
    return cast(TimecodeBurninPosition, data)
