"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Mpeg2 Adaptive Quantization"""
Mpeg2AdaptiveQuantization: TypeAlias = Literal[
    "AUTO",
    "HIGH",
    "LOW",
    "MEDIUM",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "HIGH",
        "LOW",
        "MEDIUM",
        "OFF",
    )
)


def serialize_json(value: Mpeg2AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2AdaptiveQuantization value: {data!r}")
    return cast(Mpeg2AdaptiveQuantization, data)
