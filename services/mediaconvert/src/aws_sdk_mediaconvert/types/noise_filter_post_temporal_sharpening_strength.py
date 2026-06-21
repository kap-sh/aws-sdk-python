"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseFilterPostTemporalSharpeningStrength``."""

from typing import Literal, TypeAlias, cast

"""Use Post temporal sharpening strength to define the amount of sharpening the transcoder applies to your output. Set Post temporal sharpening strength to Low, Medium, or High to indicate the amount of sharpening."""
NoiseFilterPostTemporalSharpeningStrength: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: NoiseFilterPostTemporalSharpeningStrength) -> str:
    return value


def deserialize_json(data: str) -> NoiseFilterPostTemporalSharpeningStrength:
    return cast(NoiseFilterPostTemporalSharpeningStrength, data)
