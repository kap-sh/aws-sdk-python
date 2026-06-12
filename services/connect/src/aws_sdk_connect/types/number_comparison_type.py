"""Generated from Smithy shape ``com.amazonaws.connect#NumberComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

NumberComparisonType: TypeAlias = Literal[
    "GREATER_OR_EQUAL",
    "GREATER",
    "LESSER_OR_EQUAL",
    "LESSER",
    "EQUAL",
    "NOT_EQUAL",
    "RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_OR_EQUAL",
        "GREATER",
        "LESSER_OR_EQUAL",
        "LESSER",
        "EQUAL",
        "NOT_EQUAL",
        "RANGE",
    )
)


def serialize_json(value: NumberComparisonType) -> str:
    return value


def deserialize_json(data: str) -> NumberComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NumberComparisonType value: {data!r}")
    return cast(NumberComparisonType, data)
