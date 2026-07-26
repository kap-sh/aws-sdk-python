"""Generated from Smithy shape ``com.amazonaws.glue#GlueSchemas``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glue_schema

GlueSchemas: TypeAlias = list["capo_glue.types.glue_schema.GlueSchema"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueSchemas) -> list:
    import capo_glue.types.glue_schema

    out: list = []
    for item in value:
        out.append(capo_glue.types.glue_schema.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GlueSchemas:
    import capo_glue.types.glue_schema

    out: GlueSchemas = []
    for item in data:
        out.append(capo_glue.types.glue_schema.deserialize_aws_json_1_1(item))
    return out
