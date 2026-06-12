"""Generated from Smithy shape ``com.amazonaws.securityhub#SeverityRating``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

SeverityRating: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )
)


def serialize_json(value: SeverityRating) -> str:
    return value


def deserialize_json(data: str) -> SeverityRating:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SeverityRating value: {data!r}")
    return cast(SeverityRating, data)
