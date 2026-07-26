"""Generated from Smithy shape ``com.amazonaws.medialive#Av1RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""Av1 Rate Control Mode"""
Av1RateControlMode: TypeAlias = Literal[
    "CBR",
    "QVBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Av1RateControlMode:
    return cast(Av1RateControlMode, data)
