"""Generated from Smithy shape ``com.amazonaws.medialive#AacCodingMode``."""

from typing import Literal, TypeAlias, cast

"""Aac Coding Mode"""
AacCodingMode: TypeAlias = Literal[
    "AD_RECEIVER_MIX",
    "CODING_MODE_1_0",
    "CODING_MODE_1_1",
    "CODING_MODE_2_0",
    "CODING_MODE_5_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacCodingMode) -> str:
    return value


def deserialize_json(data: str) -> AacCodingMode:
    return cast(AacCodingMode, data)
