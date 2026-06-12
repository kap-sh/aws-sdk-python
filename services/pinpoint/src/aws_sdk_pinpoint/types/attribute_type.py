"""Generated from Smithy shape ``com.amazonaws.pinpoint#AttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

AttributeType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEFORE",
    "AFTER",
    "ON",
    "BETWEEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUSIVE",
        "EXCLUSIVE",
        "CONTAINS",
        "BEFORE",
        "AFTER",
        "ON",
        "BETWEEN",
    )
)


def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeType value: {data!r}")
    return cast(AttributeType, data)
