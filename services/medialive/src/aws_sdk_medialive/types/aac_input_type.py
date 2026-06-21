"""Generated from Smithy shape ``com.amazonaws.medialive#AacInputType``."""

from typing import Literal, TypeAlias, cast

"""Aac Input Type"""
AacInputType: TypeAlias = Literal[
    "BROADCASTER_MIXED_AD",
    "NORMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacInputType) -> str:
    return value


def deserialize_json(data: str) -> AacInputType:
    return cast(AacInputType, data)
