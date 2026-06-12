"""Generated from Smithy shape ``com.amazonaws.medialive#H264AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Adaptive Quantization"""
H264AdaptiveQuantization: TypeAlias = Literal[
    "AUTO",
    "HIGH",
    "HIGHER",
    "LOW",
    "MAX",
    "MEDIUM",
    "OFF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "HIGH",
        "HIGHER",
        "LOW",
        "MAX",
        "MEDIUM",
        "OFF",
    )
)


def serialize_json(value: H264AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H264AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264AdaptiveQuantization value: {data!r}")
    return cast(H264AdaptiveQuantization, data)
