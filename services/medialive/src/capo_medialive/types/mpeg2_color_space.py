"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2ColorSpace``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Color Space"""
Mpeg2ColorSpace: TypeAlias = Literal[
    "AUTO",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2ColorSpace) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2ColorSpace:
    return cast(Mpeg2ColorSpace, data)
