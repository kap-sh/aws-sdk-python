"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

SchemaStatus: TypeAlias = Literal[
    "READY",
    "NOT_READY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> SchemaStatus:
    return cast(SchemaStatus, data)
