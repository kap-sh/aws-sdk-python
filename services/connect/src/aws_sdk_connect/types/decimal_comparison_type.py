"""Generated from Smithy shape ``com.amazonaws.connect#DecimalComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DecimalComparisonType: TypeAlias = Literal[
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


def serialize_json(value: DecimalComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DecimalComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecimalComparisonType value: {data!r}")
    return cast(DecimalComparisonType, data)
