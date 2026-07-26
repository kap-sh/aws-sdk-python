"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""Mpeg2 Adaptive Quantization"""
Mpeg2AdaptiveQuantization: TypeAlias = Literal[
    "AUTO",
    "HIGH",
    "LOW",
    "MEDIUM",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2AdaptiveQuantization:
    return cast(Mpeg2AdaptiveQuantization, data)
