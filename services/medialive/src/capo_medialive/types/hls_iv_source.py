"""Generated from Smithy shape ``com.amazonaws.medialive#HlsIvSource``."""

from typing import Literal, TypeAlias, cast

"""Hls Iv Source"""
HlsIvSource: TypeAlias = Literal[
    "EXPLICIT",
    "FOLLOWS_SEGMENT_NUMBER",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsIvSource) -> str:
    return value


def deserialize_json(data: str) -> HlsIvSource:
    return cast(HlsIvSource, data)
