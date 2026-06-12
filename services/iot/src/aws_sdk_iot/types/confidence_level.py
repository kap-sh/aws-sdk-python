"""Generated from Smithy shape ``com.amazonaws.iot#ConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ConfidenceLevel: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: ConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfidenceLevel value: {data!r}")
    return cast(ConfidenceLevel, data)
