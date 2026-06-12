"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

PropertyDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DOUBLE",
    "BOOLEAN",
    "STRUCT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "INTEGER",
        "DOUBLE",
        "BOOLEAN",
        "STRUCT",
    )
)


def serialize_json(value: PropertyDataType) -> str:
    return value


def deserialize_json(data: str) -> PropertyDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyDataType value: {data!r}")
    return cast(PropertyDataType, data)
