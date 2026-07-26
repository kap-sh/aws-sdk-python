"""Generated from Smithy shape ``com.amazonaws.medialive#HlsProgramDateTimeClock``."""

from typing import Literal, TypeAlias, cast

"""Hls Program Date Time Clock"""
HlsProgramDateTimeClock: TypeAlias = Literal[
    "INITIALIZE_FROM_OUTPUT_TIMECODE",
    "SYSTEM_CLOCK",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsProgramDateTimeClock) -> str:
    return value


def deserialize_json(data: str) -> HlsProgramDateTimeClock:
    return cast(HlsProgramDateTimeClock, data)
