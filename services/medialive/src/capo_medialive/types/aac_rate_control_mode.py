"""Generated from Smithy shape ``com.amazonaws.medialive#AacRateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Aac Rate Control Mode"""
AacRateControlMode: TypeAlias = Literal[
    "CBR",
    "VBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacRateControlMode) -> str:
    return value


def deserialize_json(data: str) -> AacRateControlMode:
    return cast(AacRateControlMode, data)
