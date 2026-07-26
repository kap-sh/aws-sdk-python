"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationAlgorithmControl``."""

from typing import Literal, TypeAlias, cast

"""When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted."""
AudioNormalizationAlgorithmControl: TypeAlias = Literal[
    "CORRECT_AUDIO",
    "MEASURE_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationAlgorithmControl) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithmControl:
    return cast(AudioNormalizationAlgorithmControl, data)
