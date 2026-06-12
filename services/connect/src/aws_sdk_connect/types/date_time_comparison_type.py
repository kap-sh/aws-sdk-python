"""Generated from Smithy shape ``com.amazonaws.connect#DateTimeComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DateTimeComparisonType: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
    "RANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "EQUAL_TO",
        "RANGE",
    )
)


def serialize_json(value: DateTimeComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DateTimeComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateTimeComparisonType value: {data!r}")
    return cast(DateTimeComparisonType, data)
