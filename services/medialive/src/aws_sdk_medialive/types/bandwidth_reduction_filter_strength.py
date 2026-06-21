"""Generated from Smithy shape ``com.amazonaws.medialive#BandwidthReductionFilterStrength``."""

from typing import Literal, TypeAlias, cast

"""Bandwidth Reduction Filter Strength"""
BandwidthReductionFilterStrength: TypeAlias = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionFilterStrength:
    return cast(BandwidthReductionFilterStrength, data)
