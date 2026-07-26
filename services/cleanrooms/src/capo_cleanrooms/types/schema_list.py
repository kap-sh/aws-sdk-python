"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.schema

SchemaList: TypeAlias = list["capo_cleanrooms.types.schema.Schema"]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaList) -> list:
    import capo_cleanrooms.types.schema

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.schema.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaList:
    import capo_cleanrooms.types.schema

    out: SchemaList = []
    for item in data:
        out.append(capo_cleanrooms.types.schema.deserialize_json(item))
    return out
