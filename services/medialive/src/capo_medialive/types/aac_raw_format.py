"""Generated from Smithy shape ``com.amazonaws.medialive#AacRawFormat``."""

from typing import Literal, TypeAlias, cast

"""Aac Raw Format"""
AacRawFormat: TypeAlias = Literal[
    "LATM_LOAS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacRawFormat) -> str:
    return value


def deserialize_json(data: str) -> AacRawFormat:
    return cast(AacRawFormat, data)
