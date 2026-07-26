"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionFormat``."""

from typing import Literal, TypeAlias, cast

SchemaVersionFormat: TypeAlias = Literal[
    "AWS",
    "ZCL",
    "CONNECTOR",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaVersionFormat) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionFormat:
    return cast(SchemaVersionFormat, data)
