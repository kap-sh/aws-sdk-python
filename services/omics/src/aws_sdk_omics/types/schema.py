"""Generated from Smithy shape ``com.amazonaws.omics#Schema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.schema_item

Schema: TypeAlias = list["aws_sdk_omics.types.schema_item.SchemaItem"]


# --- restJson1 ser/de ---
def serialize_json(value: Schema) -> list:
    import aws_sdk_omics.types.schema_item

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.schema_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> Schema:
    import aws_sdk_omics.types.schema_item

    out: Schema = []
    for item in data:
        out.append(aws_sdk_omics.types.schema_item.deserialize_json(item))
    return out
