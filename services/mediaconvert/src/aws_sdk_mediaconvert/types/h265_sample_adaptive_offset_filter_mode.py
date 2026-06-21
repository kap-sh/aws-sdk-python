"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265SampleAdaptiveOffsetFilterMode``."""

from typing import Literal, TypeAlias, cast

"""Specify Sample Adaptive Offset (SAO) filter strength. Adaptive mode dynamically selects best strength based on content"""
H265SampleAdaptiveOffsetFilterMode: TypeAlias = Literal[
    "DEFAULT",
    "ADAPTIVE",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265SampleAdaptiveOffsetFilterMode) -> str:
    return value


def deserialize_json(data: str) -> H265SampleAdaptiveOffsetFilterMode:
    return cast(H265SampleAdaptiveOffsetFilterMode, data)
