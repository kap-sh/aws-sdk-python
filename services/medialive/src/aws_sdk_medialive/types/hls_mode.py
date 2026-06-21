"""Generated from Smithy shape ``com.amazonaws.medialive#HlsMode``."""

from typing import Literal, TypeAlias, cast

"""Hls Mode"""
HlsMode: TypeAlias = Literal[
    "LIVE",
    "VOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsMode) -> str:
    return value


def deserialize_json(data: str) -> HlsMode:
    return cast(HlsMode, data)
