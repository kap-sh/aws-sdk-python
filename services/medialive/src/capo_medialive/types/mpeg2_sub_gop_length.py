"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2SubGopLength``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Sub Gop Length"""
Mpeg2SubGopLength: TypeAlias = Literal[
    "DYNAMIC",
    "FIXED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2SubGopLength) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2SubGopLength:
    return cast(Mpeg2SubGopLength, data)
