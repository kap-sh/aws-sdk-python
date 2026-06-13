"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehubv2.errors import DeserializationError

FindingSeverity: TypeAlias = Literal[
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


def serialize_json(value: FindingSeverity) -> str:
    return value


def deserialize_json(data: str) -> FindingSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingSeverity value: {data!r}")
    return cast(FindingSeverity, data)
