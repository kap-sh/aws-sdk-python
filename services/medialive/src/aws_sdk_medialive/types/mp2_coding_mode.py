"""Generated from Smithy shape ``com.amazonaws.medialive#Mp2CodingMode``."""

from typing import Literal, TypeAlias, cast

"""Mp2 Coding Mode"""
Mp2CodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mp2CodingMode) -> str:
    return value


def deserialize_json(data: str) -> Mp2CodingMode:
    return cast(Mp2CodingMode, data)
