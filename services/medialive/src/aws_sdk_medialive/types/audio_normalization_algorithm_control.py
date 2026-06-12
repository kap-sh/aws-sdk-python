"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationAlgorithmControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Normalization Algorithm Control"""
AudioNormalizationAlgorithmControl: TypeAlias = Literal["CORRECT_AUDIO",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CORRECT_AUDIO",))


def serialize_json(value: AudioNormalizationAlgorithmControl) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithmControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioNormalizationAlgorithmControl value: {data!r}"
        )
    return cast(AudioNormalizationAlgorithmControl, data)
