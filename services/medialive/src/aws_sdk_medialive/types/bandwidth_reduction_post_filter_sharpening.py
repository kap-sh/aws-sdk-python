"""Generated from Smithy shape ``com.amazonaws.medialive#BandwidthReductionPostFilterSharpening``."""

from typing import Literal, TypeAlias, cast

"""Bandwidth Reduction Post Filter Sharpening"""
BandwidthReductionPostFilterSharpening: TypeAlias = Literal[
    "DISABLED",
    "SHARPENING_1",
    "SHARPENING_2",
    "SHARPENING_3",
]


# --- restJson1 ser/de ---
def serialize_json(value: BandwidthReductionPostFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionPostFilterSharpening:
    return cast(BandwidthReductionPostFilterSharpening, data)
