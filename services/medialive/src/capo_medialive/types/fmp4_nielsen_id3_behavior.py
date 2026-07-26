"""Generated from Smithy shape ``com.amazonaws.medialive#Fmp4NielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

"""Fmp4 Nielsen Id3 Behavior"""
Fmp4NielsenId3Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Fmp4NielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> Fmp4NielsenId3Behavior:
    return cast(Fmp4NielsenId3Behavior, data)
