"""Generated from Smithy shape ``com.amazonaws.devopsguru#InsightSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

InsightSeverity: TypeAlias = Literal[
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


def serialize_json(value: InsightSeverity) -> str:
    return value


def deserialize_json(data: str) -> InsightSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InsightSeverity value: {data!r}")
    return cast(InsightSeverity, data)
