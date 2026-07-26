"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyDataType``."""

from typing import Literal, TypeAlias, cast

PropertyDataType: TypeAlias = Literal[
    "STRING",
    "INTEGER",
    "DOUBLE",
    "BOOLEAN",
    "STRUCT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PropertyDataType) -> str:
    return value


def deserialize_json(data: str) -> PropertyDataType:
    return cast(PropertyDataType, data)
