"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInAlignment``."""

from typing import Literal, TypeAlias, cast

"""Burn In Alignment"""
BurnInAlignment: TypeAlias = Literal[
    "CENTERED",
    "LEFT",
    "SMART",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInAlignment) -> str:
    return value


def deserialize_json(data: str) -> BurnInAlignment:
    return cast(BurnInAlignment, data)
