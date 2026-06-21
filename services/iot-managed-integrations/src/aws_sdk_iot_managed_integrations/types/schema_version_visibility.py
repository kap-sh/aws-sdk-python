"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchemaVersionVisibility``."""

from typing import Literal, TypeAlias, cast

SchemaVersionVisibility: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaVersionVisibility) -> str:
    return value


def deserialize_json(data: str) -> SchemaVersionVisibility:
    return cast(SchemaVersionVisibility, data)
