"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Audio Normalization Algorithm"""
AudioNormalizationAlgorithm: TypeAlias = Literal[
    "ITU_1770_1",
    "ITU_1770_2",
    "ITU_1770_3",
    "ITU_1770_4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ITU_1770_1",
        "ITU_1770_2",
        "ITU_1770_3",
        "ITU_1770_4",
    )
)


def serialize_json(value: AudioNormalizationAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> AudioNormalizationAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AudioNormalizationAlgorithm value: {data!r}"
        )
    return cast(AudioNormalizationAlgorithm, data)
