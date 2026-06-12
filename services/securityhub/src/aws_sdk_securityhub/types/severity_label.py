"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityLabel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

SeverityLabel: TypeAlias = Literal[
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


def serialize_json(value: SeverityLabel) -> str:
    return value


def deserialize_json(data: str) -> SeverityLabel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SeverityLabel value: {data!r}")
    return cast(SeverityLabel, data)
