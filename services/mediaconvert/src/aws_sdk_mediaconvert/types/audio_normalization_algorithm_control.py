"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationAlgorithmControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted."""
AudioNormalizationAlgorithmControl: TypeAlias = Literal[
    "CORRECT_AUDIO",
    "MEASURE_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CORRECT_AUDIO",
        "MEASURE_ONLY",
    )
)


def serialize_json(value: AudioNormalizationAlgorithmControl) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithmControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioNormalizationAlgorithmControl value: {data!r}"
        )
    return cast(AudioNormalizationAlgorithmControl, data)
