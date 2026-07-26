"""Generated from Smithy shape ``com.amazonaws.entityresolution#Schemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.schema_list

Schemas: TypeAlias = list["capo_entityresolution.types.schema_list.SchemaList"]


# --- restJson1 ser/de ---
def serialize_json(value: Schemas) -> list:
    import capo_entityresolution.types.schema_list

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.schema_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> Schemas:
    import capo_entityresolution.types.schema_list

    out: Schemas = []
    for item in data:
        out.append(capo_entityresolution.types.schema_list.deserialize_json(item))
    return out
