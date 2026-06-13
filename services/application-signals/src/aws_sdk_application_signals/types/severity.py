"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Severity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

Severity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CRITICAL",
        "HIGH",
        "MEDIUM",
        "LOW",
        "NONE",
    )
)


def serialize_json(value: Severity) -> str:
    return value


def deserialize_json(data: str) -> Severity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Severity value: {data!r}")
    return cast(Severity, data)
