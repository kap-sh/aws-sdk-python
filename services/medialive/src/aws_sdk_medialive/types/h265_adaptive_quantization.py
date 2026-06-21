"""Generated from Smithy shape ``com.amazonaws.medialive#H265AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

"""H265 Adaptive Quantization"""
H265AdaptiveQuantization: TypeAlias = Literal[
    "AUTO",
    "HIGH",
    "HIGHER",
    "LOW",
    "MAX",
    "MEDIUM",
    "OFF",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H265AdaptiveQuantization:
    return cast(H265AdaptiveQuantization, data)
