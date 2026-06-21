"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaType``."""

from typing import Literal, TypeAlias, cast

SchemaType: TypeAlias = Literal[
    "TABLE",
    "ID_MAPPING_TABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaType) -> str:
    return value


def deserialize_json(data: str) -> SchemaType:
    return cast(SchemaType, data)
