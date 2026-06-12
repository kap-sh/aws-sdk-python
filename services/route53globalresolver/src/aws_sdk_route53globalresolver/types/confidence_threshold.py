"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ConfidenceThreshold``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

ConfidenceThreshold: TypeAlias = Literal[
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


def serialize_json(value: ConfidenceThreshold) -> str:
    return value


def deserialize_json(data: str) -> ConfidenceThreshold:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfidenceThreshold value: {data!r}")
    return cast(ConfidenceThreshold, data)
