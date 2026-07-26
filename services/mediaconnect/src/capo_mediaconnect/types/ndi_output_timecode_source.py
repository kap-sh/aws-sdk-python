"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiOutputTimecodeSource``."""

from typing import Literal, TypeAlias, cast

NdiOutputTimecodeSource: TypeAlias = Literal[
    "EMBEDDED_TIMECODE",
    "UTC_SYSTEM_TIME",
]


# --- restJson1 ser/de ---
def serialize_json(value: NdiOutputTimecodeSource) -> str:
    return value


def deserialize_json(data: str) -> NdiOutputTimecodeSource:
    return cast(NdiOutputTimecodeSource, data)
