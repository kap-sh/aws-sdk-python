"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationPeakCalculation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Normalization Peak Calculation"""
AudioNormalizationPeakCalculation: TypeAlias = Literal[
    "NONE",
    "TRUE_PEAK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "TRUE_PEAK",
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
