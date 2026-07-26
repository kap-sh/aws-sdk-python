"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3CodingMode``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Coding Mode"""
Eac3CodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
    "CODING_MODE_3_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3CodingMode:
    return cast(Eac3CodingMode, data)
