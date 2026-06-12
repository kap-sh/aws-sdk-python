"""Generated from Smithy shape ``com.amazonaws.devopsguru#AnomalySeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

AnomalySeverity: TypeAlias = Literal[
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


def serialize_json(value: AnomalySeverity) -> str:
    return value


def deserialize_json(data: str) -> AnomalySeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalySeverity value: {data!r}")
    return cast(AnomalySeverity, data)
