"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

SchemaVersionVisibility: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE",
    )
)


def serialize_json(value: SchemaVersionVisibility) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchemaVersionVisibility value: {data!r}")
    return cast(SchemaVersionVisibility, data)
