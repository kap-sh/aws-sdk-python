"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInBackgroundColor``."""

from typing import Literal, TypeAlias, cast

"""Burn In Background Color"""
BurnInBackgroundColor: TypeAlias = Literal[
    "BLACK",
    "NONE",
    "WHITE",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInBackgroundColor) -> str:
    return value


def deserialize_json(data: str) -> BurnInBackgroundColor:
    return cast(BurnInBackgroundColor, data)
