"""Generated from Smithy shape ``com.amazonaws.medialive#HlsDefault``."""

from typing import Literal, TypeAlias, cast

"""Hls Default"""
HlsDefault: TypeAlias = Literal[
    "NO",
    "OMIT",
    "YES",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsDefault) -> str:
    return value


def deserialize_json(data: str) -> HlsDefault:
    return cast(HlsDefault, data)
