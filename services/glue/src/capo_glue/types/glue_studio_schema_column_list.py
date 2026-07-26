"""Generated from Smithy shape ``com.amazonaws.glue#GlueStudioSchemaColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glue_studio_schema_column

GlueStudioSchemaColumnList: TypeAlias = list[
    "capo_glue.types.glue_studio_schema_column.GlueStudioSchemaColumn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueStudioSchemaColumnList) -> list:
    import capo_glue.types.glue_studio_schema_column

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.glue_studio_schema_column.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GlueStudioSchemaColumnList:
    import capo_glue.types.glue_studio_schema_column

    out: GlueStudioSchemaColumnList = []
    for item in data:
        out.append(
            capo_glue.types.glue_studio_schema_column.deserialize_aws_json_1_1(item)
        )
    return out
