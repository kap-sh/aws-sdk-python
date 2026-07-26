"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosSurroundExMode``."""

from typing import Literal, TypeAlias, cast

"""Specify whether your input audio has an additional center rear surround channel matrix encoded into your left and right surround channels."""
Eac3AtmosSurroundExMode: TypeAlias = Literal[
    "NOT_INDICATED",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosSurroundExMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosSurroundExMode:
    return cast(Eac3AtmosSurroundExMode, data)
