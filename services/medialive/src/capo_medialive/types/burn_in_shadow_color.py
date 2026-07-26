"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInShadowColor``."""

from typing import Literal, TypeAlias, cast

"""Burn In Shadow Color"""
BurnInShadowColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInShadowColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInShadowColor:
    return cast(BurnInShadowColor, data)
