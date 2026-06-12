"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

SchemaVersionFormat: TypeAlias = Literal[
    "AWS",
    "ZCL",
    "CONNECTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "ZCL",
        "CONNECTOR",
    )
)


def serialize_json(value: SchemaVersionFormat) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaVersionFormat value: {data!r}")
    return cast(SchemaVersionFormat, data)
