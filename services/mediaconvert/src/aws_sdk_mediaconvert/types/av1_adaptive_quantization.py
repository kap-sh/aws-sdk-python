"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization."""
Av1AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGHER",
    "MAX",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Av1AdaptiveQuantization:
    return cast(Av1AdaptiveQuantization, data)
