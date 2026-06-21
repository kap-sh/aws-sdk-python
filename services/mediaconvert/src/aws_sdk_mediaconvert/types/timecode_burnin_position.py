"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimecodeBurninPosition``."""

from typing import Literal, TypeAlias, cast

"""Use Position under Timecode burn-in to specify the location the burned-in timecode on output video."""
TimecodeBurninPosition: TypeAlias = Literal[
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",
    "MIDDLE_LEFT",
    "MIDDLE_CENTER",
    "MIDDLE_RIGHT",
    "BOTTOM_LEFT",
    "BOTTOM_CENTER",
    "BOTTOM_RIGHT",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurninPosition) -> str:
    return value


def deserialize_json(data: str) -> TimecodeBurninPosition:
    return cast(TimecodeBurninPosition, data)
