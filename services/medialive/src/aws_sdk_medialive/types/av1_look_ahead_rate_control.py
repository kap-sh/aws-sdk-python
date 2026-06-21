"""Generated from Smithy shape ``com.amazonaws.medialive#Av1LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

"""Av1 Look Ahead Rate Control"""
Av1LookAheadRateControl: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> Av1LookAheadRateControl:
    return cast(Av1LookAheadRateControl, data)
