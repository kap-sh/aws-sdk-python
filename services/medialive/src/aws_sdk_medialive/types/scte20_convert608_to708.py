"""Generated from Smithy shape ``com.amazonaws.medialive#Scte20Convert608To708``."""

from typing import Literal, TypeAlias, cast

"""Scte20 Convert608 To708"""
Scte20Convert608To708: TypeAlias = Literal[
    "DISABLED",
    "UPCONVERT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Scte20Convert608To708) -> str:
    return value


def deserialize_json(data: str) -> Scte20Convert608To708:
    return cast(Scte20Convert608To708, data)
