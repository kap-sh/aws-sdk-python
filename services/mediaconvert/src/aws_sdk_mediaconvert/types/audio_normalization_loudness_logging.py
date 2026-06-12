"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationLoudnessLogging``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If set to LOG, log each output's audio track loudness to a CSV file."""
AudioNormalizationLoudnessLogging: TypeAlias = Literal[
    "LOG",
    "DONT_LOG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOG",
        "DONT_LOG",
    )
)


def serialize_json(value: AudioNormalizationLoudnessLogging) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationLoudnessLogging:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioNormalizationLoudnessLogging value: {data!r}"
        )
    return cast(AudioNormalizationLoudnessLogging, data)
