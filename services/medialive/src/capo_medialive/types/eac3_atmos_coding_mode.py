"""Generated from Smithy shape ``com.amazonaws.medialive#Eac3AtmosCodingMode``."""

from typing import Literal, TypeAlias, cast

"""Eac3 Atmos Coding Mode"""
Eac3AtmosCodingMode: TypeAlias = Literal[
    "CODING_MODE_5_1_4",
    "CODING_MODE_7_1_4",
    "CODING_MODE_9_1_6",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3AtmosCodingMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosCodingMode:
    return cast(Eac3AtmosCodingMode, data)
