"""Generated from Smithy shape ``com.amazonaws.medialive#TemporalFilterStrength``."""

from typing import Literal, TypeAlias, cast

"""Temporal Filter Strength"""
TemporalFilterStrength: TypeAlias = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
    "STRENGTH_5",
    "STRENGTH_6",
    "STRENGTH_7",
    "STRENGTH_8",
    "STRENGTH_9",
    "STRENGTH_10",
    "STRENGTH_11",
    "STRENGTH_12",
    "STRENGTH_13",
    "STRENGTH_14",
    "STRENGTH_15",
    "STRENGTH_16",
]


# --- restJson1 ser/de ---
def serialize_json(value: TemporalFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> TemporalFilterStrength:
    return cast(TemporalFilterStrength, data)
