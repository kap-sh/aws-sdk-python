"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

SchemaStatus: TypeAlias = Literal[
    "READY",
    "NOT_READY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "NOT_READY",
    )
)


def serialize_json(value: SchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> SchemaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaStatus value: {data!r}")
    return cast(SchemaStatus, data)
