"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to the following settings: Spatial adaptive quantization, and Temporal adaptive quantization."""
Mpeg2AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: Mpeg2AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2AdaptiveQuantization value: {data!r}")
    return cast(Mpeg2AdaptiveQuantization, data)
