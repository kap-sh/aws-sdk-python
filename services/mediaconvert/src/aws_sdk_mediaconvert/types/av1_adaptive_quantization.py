"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the strength of any adaptive quantization filters that you enable. The value that you choose here applies to Spatial adaptive quantization."""
Av1AdaptiveQuantization: TypeAlias = Literal[
    "OFF",
    "LOW",
    "MEDIUM",
    "HIGH",
    "HIGHER",
    "MAX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "LOW",
        "MEDIUM",
        "HIGH",
        "HIGHER",
        "MAX",
    )
)


def serialize_json(value: Av1AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Av1AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Av1AdaptiveQuantization value: {data!r}")
    return cast(Av1AdaptiveQuantization, data)
