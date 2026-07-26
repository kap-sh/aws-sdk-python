"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationAlgorithm``."""

from typing import Literal, TypeAlias, cast

"""Audio Normalization Algorithm"""
AudioNormalizationAlgorithm: TypeAlias = Literal[
    "ITU_1770_1",
    "ITU_1770_2",
    "ITU_1770_3",
    "ITU_1770_4",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithm:
    return cast(AudioNormalizationAlgorithm, data)
