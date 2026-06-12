"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DateDimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

DateDimensionType: TypeAlias = Literal[
    "BEFORE",
    "AFTER",
    "BETWEEN",
    "NOT_BETWEEN",
    "ON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE",
        "AFTER",
        "BETWEEN",
        "NOT_BETWEEN",
        "ON",
    )
)


def serialize_json(value: DateDimensionType) -> str:
    return value


def deserialize_json(data: str) -> DateDimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateDimensionType value: {data!r}")
    return cast(DateDimensionType, data)
