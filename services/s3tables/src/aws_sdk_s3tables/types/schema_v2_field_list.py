"""Generated from Smithy shape ``com.amazonaws.s3tables#SchemaV2FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.schema_v2_field

SchemaV2FieldList: TypeAlias = list[
    "aws_sdk_s3tables.types.schema_v2_field.SchemaV2Field"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaV2FieldList) -> list:
    import aws_sdk_s3tables.types.schema_v2_field

    out: list = []
    for item in value:
        out.append(aws_sdk_s3tables.types.schema_v2_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> SchemaV2FieldList:
    import aws_sdk_s3tables.types.schema_v2_field

    out: SchemaV2FieldList = []
    for item in data:
        out.append(aws_sdk_s3tables.types.schema_v2_field.deserialize_json(item))
    return out
