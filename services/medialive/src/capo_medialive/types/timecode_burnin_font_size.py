"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeBurninFontSize``."""

from typing import Literal, TypeAlias, cast

"""Timecode Burnin Font Size"""
TimecodeBurninFontSize: TypeAlias = Literal[
    "EXTRA_SMALL_10",
    "LARGE_48",
    "MEDIUM_32",
    "SMALL_16",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeBurninFontSize) -> str:
    return value


def deserialize_json(data: str) -> TimecodeBurninFontSize:
    return cast(TimecodeBurninFontSize, data)
