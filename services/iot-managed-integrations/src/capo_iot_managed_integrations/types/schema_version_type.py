"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionType``."""

from typing import Literal, TypeAlias, cast

SchemaVersionType: TypeAlias = Literal[
    "capability",
    "definition",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaVersionType) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionType:
    return cast(SchemaVersionType, data)
