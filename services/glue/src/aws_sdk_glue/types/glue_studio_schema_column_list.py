"""Generated from Smithy shape ``com.amazonaws.glue#GlueStudioSchemaColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_studio_schema_column

GlueStudioSchemaColumnList: TypeAlias = list[
    "aws_sdk_glue.types.glue_studio_schema_column.GlueStudioSchemaColumn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueStudioSchemaColumnList) -> list:
    import aws_sdk_glue.types.glue_studio_schema_column

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.glue_studio_schema_column.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GlueStudioSchemaColumnList:
    import aws_sdk_glue.types.glue_studio_schema_column

    out: GlueStudioSchemaColumnList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.glue_studio_schema_column.deserialize_aws_json_1_1(item)
        )
    return out
