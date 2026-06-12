"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationPeakCalculation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If set to TRUE_PEAK, calculate and log the TruePeak for each output's audio track loudness."""
AudioNormalizationPeakCalculation: TypeAlias = Literal[
    "TRUE_PEAK",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE_PEAK",
        "NONE",
    )
)


def serialize_json(value: AudioNormalizationPeakCalculation) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationPeakCalculation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioNormalizationPeakCalculation value: {data!r}"
        )
    return cast(AudioNormalizationPeakCalculation, data)
