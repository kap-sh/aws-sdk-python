"""Generated from Smithy shape ``com.amazonaws.lambda#SchemaRegistryEventRecordFormat``."""

from typing import Literal, TypeAlias, cast

SchemaRegistryEventRecordFormat: TypeAlias = Literal[
    "JSON",
    "SOURCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaRegistryEventRecordFormat) -> str:
    return value


def deserialize_json(data: str) -> SchemaRegistryEventRecordFormat:
    return cast(SchemaRegistryEventRecordFormat, data)
