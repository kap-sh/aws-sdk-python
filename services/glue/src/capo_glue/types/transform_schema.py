"""Generated from Smithy shape ``com.amazonaws.glue#TransformSchema``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.schema_column

TransformSchema: TypeAlias = list["capo_glue.types.schema_column.SchemaColumn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformSchema) -> list:
    import capo_glue.types.schema_column

    out: list = []
    for item in value:
        out.append(capo_glue.types.schema_column.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TransformSchema:
    import capo_glue.types.schema_column

    out: TransformSchema = []
    for item in data:
        out.append(capo_glue.types.schema_column.deserialize_aws_json_1_1(item))
    return out
