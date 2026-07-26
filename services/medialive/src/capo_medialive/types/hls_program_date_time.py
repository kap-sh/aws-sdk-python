"""Generated from Smithy shape ``com.amazonaws.medialive#HlsProgramDateTime``."""

from typing import Literal, TypeAlias, cast

"""Hls Program Date Time"""
HlsProgramDateTime: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsProgramDateTime) -> str:
    return value


def deserialize_json(data: str) -> HlsProgramDateTime:
    return cast(HlsProgramDateTime, data)
