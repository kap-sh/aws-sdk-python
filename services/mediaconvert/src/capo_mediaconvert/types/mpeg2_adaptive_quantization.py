"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization."""
Mpeg2AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2AdaptiveQuantization:
    return cast(Mpeg2AdaptiveQuantization, data)
