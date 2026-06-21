"""Generated from Smithy shape ``com.amazonaws.medialive#HlsAutoSelect``."""

from typing import Literal, TypeAlias, cast

"""Hls Auto Select"""
HlsAutoSelect: TypeAlias = Literal[
    "NO",
    "OMIT",
    "YES",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsAutoSelect) -> str:
    return value


def deserialize_json(data: str) -> HlsAutoSelect:
    return cast(HlsAutoSelect, data)
