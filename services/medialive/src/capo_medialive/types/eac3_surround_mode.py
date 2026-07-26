"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3SurroundMode``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Surround Mode"""
Eac3SurroundMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "NOT_INDICATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3SurroundMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundMode:
    return cast(Eac3SurroundMode, data)
