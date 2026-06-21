"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInFontColor``."""

from typing import Literal, TypeAlias, cast

"""Burn In Font Color"""
BurnInFontColor: TypeAlias = Literal[
    "BLACK",
    "BLUE",
    "GREEN",
    "RED",
    "WHITE",
    "YELLOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInFontColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInFontColor:
    return cast(BurnInFontColor, data)
