"""Generated from Smithy shape ``com.amazonaws.medialive#H265AdaptiveQuantization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Adaptive Quantization"""
H265AdaptiveQuantization: TypeAlias = Literal[
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


def serialize_json(value: H265AdaptiveQuantization) -> str:
    return value


def deserialize_json(data: str) -> H265AdaptiveQuantization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265AdaptiveQuantization value: {data!r}")
    return cast(H265AdaptiveQuantization, data)
