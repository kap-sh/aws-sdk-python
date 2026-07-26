"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SchemaType``."""

from typing import Literal, TypeAlias, cast

SchemaType: TypeAlias = Literal[
    "string",
    "number",
    "object",
    "array",
    "boolean",
    "integer",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaType) -> str:
    return value


def deserialize_json(data: str) -> SchemaType:
    return cast(SchemaType, data)
