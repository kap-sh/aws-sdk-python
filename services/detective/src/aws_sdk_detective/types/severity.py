"""Generated from Smithy shape ``com.amazonaws.detective#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

Severity: TypeAlias = Literal[
    "INFORMATIONAL",
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFORMATIONAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )
)


def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
