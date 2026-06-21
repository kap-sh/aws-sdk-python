"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationAlgorithmControl``."""

from typing import Literal, TypeAlias, cast

"""Audio Normalization Algorithm Control"""
AudioNormalizationAlgorithmControl: TypeAlias = Literal["CORRECT_AUDIO",]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationAlgorithmControl) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithmControl:
    return cast(AudioNormalizationAlgorithmControl, data)
