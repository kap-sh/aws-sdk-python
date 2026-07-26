"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3PassthroughControl``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Passthrough Control"""
Eac3PassthroughControl: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "WHEN_POSSIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3PassthroughControl) -> str:
    return value


def deserialize_json(data: str) -> Eac3PassthroughControl:
    return cast(Eac3PassthroughControl, data)
