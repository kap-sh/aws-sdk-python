"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp8QualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, multi-pass encoding."""
Vp8QualityTuningLevel: TypeAlias = Literal[
    "MULTI_PASS",
    "MULTI_PASS_HQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: Vp8QualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Vp8QualityTuningLevel:
    return cast(Vp8QualityTuningLevel, data)
