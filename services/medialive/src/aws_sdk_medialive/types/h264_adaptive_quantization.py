"""Generated from Smithy shape ``com.amazonaws.medialive#H264AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""H264 Adaptive Quantization"""
H264AdaptiveQuantization: TypeAlias = Literal[
    "AUTO",
    "HIGH",
    "HIGHER",
    "LOW",
    "MAX",
    "MEDIUM",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H264AdaptiveQuantization:
    return cast(H264AdaptiveQuantization, data)
