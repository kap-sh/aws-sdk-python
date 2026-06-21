"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationPeakCalculation``."""

from typing import Literal, TypeAlias, cast

"""If set to TRUE_PEAK, calculate and log the TruePeak for each output's audio track loudness."""
AudioNormalizationPeakCalculation: TypeAlias = Literal[
    "TRUE_PEAK",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationPeakCalculation) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationPeakCalculation:
    return cast(AudioNormalizationPeakCalculation, data)
