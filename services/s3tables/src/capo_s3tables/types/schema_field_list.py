"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.schema_field

SchemaFieldList: TypeAlias = list["capo_s3tables.types.schema_field.SchemaField"]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaFieldList) -> list:
    import capo_s3tables.types.schema_field

    out: list = []
    for item in value:
        out.append(capo_s3tables.types.schema_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaFieldList:
    import capo_s3tables.types.schema_field

    out: SchemaFieldList = []
    for item in data:
        out.append(capo_s3tables.types.schema_field.deserialize_json(item))
    return out
