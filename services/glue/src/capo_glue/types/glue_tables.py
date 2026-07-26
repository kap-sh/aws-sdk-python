"""Generated from Smithy shape ``com.amazonaws.glue#GlueTables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.glue_table

GlueTables: TypeAlias = list["capo_glue.types.glue_table.GlueTable"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueTables) -> list:
    import capo_glue.types.glue_table

    out: list = []
    for item in value:
        out.append(capo_glue.types.glue_table.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GlueTables:
    import capo_glue.types.glue_table

    out: GlueTables = []
    for item in data:
        out.append(capo_glue.types.glue_table.deserialize_aws_json_1_1(item))
    return out
