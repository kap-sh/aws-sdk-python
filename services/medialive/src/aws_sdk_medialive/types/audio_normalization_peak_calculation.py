"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationPeakCalculation``."""

from typing import Literal, TypeAlias, cast

"""Audio Normalization Peak Calculation"""
AudioNormalizationPeakCalculation: TypeAlias = Literal[
    "NONE",
    "TRUE_PEAK",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationPeakCalculation) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationPeakCalculation:
    return cast(AudioNormalizationPeakCalculation, data)
