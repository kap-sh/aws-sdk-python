"""Generated from Smithy shape ``com.amazonaws.iot#DynamoKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

DynamoKeyType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "NUMBER",
    )
)


def serialize_json(value: DynamoKeyType) -> str:
    return value


def deserialize_json(data: str) -> DynamoKeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DynamoKeyType value: {data!r}")
    return cast(DynamoKeyType, data)
