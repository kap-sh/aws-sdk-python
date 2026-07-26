"""Generated from Smithy shape ``com.amazonaws.medialive#BurnInTeletextGridControl``."""

from typing import Literal, TypeAlias, cast

"""Burn In Teletext Grid Control"""
BurnInTeletextGridControl: TypeAlias = Literal[
    "FIXED",
    "SCALED",
]


# --- restJson1 ser/de ---
def serialize_json(value: BurnInTeletextGridControl) -> str:
    return value


def deserialize_json(data: str) -> BurnInTeletextGridControl:
    return cast(BurnInTeletextGridControl, data)
