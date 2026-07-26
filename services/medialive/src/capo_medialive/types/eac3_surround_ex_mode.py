"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3SurroundExMode``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Surround Ex Mode"""
Eac3SurroundExMode: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "NOT_INDICATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3SurroundExMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundExMode:
    return cast(Eac3SurroundExMode, data)
