"""Generated from Smithy shape ``com.amazonaws.connect#DateComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DateComparisonType: TypeAlias = Literal[
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL_TO",
    "LESS_THAN_OR_EQUAL_TO",
    "EQUAL_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_OR_EQUAL_TO",
        "LESS_THAN_OR_EQUAL_TO",
        "EQUAL_TO",
    )
)


def serialize_json(value: DateComparisonType) -> str:
    return value


def deserialize_json(data: str) -> DateComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateComparisonType value: {data!r}")
    return cast(DateComparisonType, data)
