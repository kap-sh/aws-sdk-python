"""Generated from Smithy shape ``com.amazonaws.medialive#TimecodeConfigSource``."""

from typing import Literal, TypeAlias, cast

"""Timecode Config Source"""
TimecodeConfigSource: TypeAlias = Literal[
    "EMBEDDED",
    "SYSTEMCLOCK",
    "ZEROBASED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeConfigSource) -> str:
    return value


def deserialize_json(data: str) -> TimecodeConfigSource:
    return cast(TimecodeConfigSource, data)
