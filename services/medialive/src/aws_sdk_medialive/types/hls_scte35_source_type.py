"""Generated from Smithy shape ``com.amazonaws.medialive#HlsScte35SourceType``."""

from typing import Literal, TypeAlias, cast

"""Hls Scte35 Source Type"""
HlsScte35SourceType: TypeAlias = Literal[
    "MANIFEST",
    "SEGMENTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsScte35SourceType) -> str:
    return value


def deserialize_json(data: str) -> HlsScte35SourceType:
    return cast(HlsScte35SourceType, data)
