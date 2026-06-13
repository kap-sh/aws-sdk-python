"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaList``."""

from typing import TypeAlias

SchemaList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaList) -> list:
    return list(value)


def deserialize_json(data: list) -> SchemaList:
    return list(data)
