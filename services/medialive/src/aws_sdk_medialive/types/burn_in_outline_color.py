"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInOutlineColor``."""

from typing import Literal, TypeAlias, cast

"""Burn In Outline Color"""
BurnInOutlineColor: TypeAlias = Literal[
    "BLACK",
    "BLUE",
    "GREEN",
    "RED",
    "WHITE",
    "YELLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInOutlineColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInOutlineColor:
    return cast(BurnInOutlineColor, data)
