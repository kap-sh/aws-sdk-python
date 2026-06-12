"""Generated from Smithy shape ``com.amazonaws.glue#GlueTables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_table

GlueTables: TypeAlias = list["aws_sdk_glue.types.glue_table.GlueTable"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueTables) -> list:
    import aws_sdk_glue.types.glue_table

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.glue_table.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GlueTables:
    import aws_sdk_glue.types.glue_table

    out: GlueTables = []
    for item in data:
        out.append(aws_sdk_glue.types.glue_table.deserialize_aws_json_1_1(item))
    return out
