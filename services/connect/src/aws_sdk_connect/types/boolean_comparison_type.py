"""Generated from Smithy shape ``com.amazonaws.connect#BooleanComparisonType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

BooleanComparisonType: TypeAlias = Literal[
    "IS_TRUE",
    "IS_FALSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IS_TRUE",
        "IS_FALSE",
    )
)


def serialize_json(value: BooleanComparisonType) -> str:
    return value


def deserialize_json(data: str) -> BooleanComparisonType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BooleanComparisonType value: {data!r}")
    return cast(BooleanComparisonType, data)
