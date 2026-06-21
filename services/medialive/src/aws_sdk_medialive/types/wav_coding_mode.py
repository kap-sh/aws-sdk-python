"""Generated from Smithy shape ``com.amazonaws.medialive#WavCodingMode``."""

from typing import Literal, TypeAlias, cast

"""Wav Coding Mode"""
WavCodingMode: TypeAlias = Literal[
    "CODING_MODE_1_0",
    "CODING_MODE_2_0",
    "CODING_MODE_4_0",
    "CODING_MODE_8_0",
]


# --- restJson1 ser/de ---
def serialize_json(value: WavCodingMode) -> str:
    return value


def deserialize_json(data: str) -> WavCodingMode:
    return cast(WavCodingMode, data)
