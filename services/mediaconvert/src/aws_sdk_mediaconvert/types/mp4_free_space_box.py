"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mp4FreeSpaceBox``."""

from typing import Literal, TypeAlias, cast

"""Inserts a free-space box immediately after the moov box."""
Mp4FreeSpaceBox: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mp4FreeSpaceBox) -> str:
    return value


def deserialize_json(data: str) -> Mp4FreeSpaceBox:
    return cast(Mp4FreeSpaceBox, data)
