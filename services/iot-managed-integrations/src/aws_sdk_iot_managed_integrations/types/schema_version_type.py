"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

SchemaVersionType: TypeAlias = Literal[
    "capability",
    "definition",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "capability",
        "definition",
    )
)


def serialize_json(value: SchemaVersionType) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaVersionType value: {data!r}")
    return cast(SchemaVersionType, data)
