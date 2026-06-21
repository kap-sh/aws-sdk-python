"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Xavc4kProfileQualityTuningLevel``."""

from typing import Literal, TypeAlias, cast

"""Optional. Use Quality tuning level to choose how you want to trade off encoding speed for output video quality. The default behavior is faster, lower quality, single-pass encoding."""
Xavc4kProfileQualityTuningLevel: TypeAlias = Literal[
    "SINGLE_PASS",
    "SINGLE_PASS_HQ",
    "MULTI_PASS_HQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: Xavc4kProfileQualityTuningLevel) -> str:
    return value


def deserialize_json(data: str) -> Xavc4kProfileQualityTuningLevel:
    return cast(Xavc4kProfileQualityTuningLevel, data)
