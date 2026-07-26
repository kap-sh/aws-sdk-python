"""Generated from Smithy shape ``com.amazonaws.omics#Schema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.schema_item

Schema: TypeAlias = list["capo_omics.types.schema_item.SchemaItem"]


# --- restJson1 ser/de ---
def serialize_json(value: Schema) -> list:
    import capo_omics.types.schema_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.schema_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> Schema:
    import capo_omics.types.schema_item

    out: Schema = []
    for item in data:
        out.append(capo_omics.types.schema_item.deserialize_json(item))
    return out
