"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeDimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

AttributeDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEGINS_WITH",
    "ENDS_WITH",
    "BEFORE",
    "AFTER",
    "BETWEEN",
    "NOT_BETWEEN",
    "ON",
    "GREATER_THAN",
    "LESS_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN_OR_EQUAL",
    "EQUAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUSIVE",
        "EXCLUSIVE",
        "CONTAINS",
        "BEGINS_WITH",
        "ENDS_WITH",
        "BEFORE",
        "AFTER",
        "BETWEEN",
        "NOT_BETWEEN",
        "ON",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN_OR_EQUAL",
        "EQUAL",
    )
)


def serialize_json(value: AttributeDimensionType) -> str:
    return value


def deserialize_json(data: str) -> AttributeDimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeDimensionType value: {data!r}")
    return cast(AttributeDimensionType, data)
