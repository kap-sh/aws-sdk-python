"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationLoudnessLogging``."""

from typing import Literal, TypeAlias, cast

"""If set to LOG, log each output's audio track loudness to a CSV file."""
AudioNormalizationLoudnessLogging: TypeAlias = Literal[
    "LOG",
    "DONT_LOG",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationLoudnessLogging) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationLoudnessLogging:
    return cast(AudioNormalizationLoudnessLogging, data)
