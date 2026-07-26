"""Generated from Smithy shape ``com.amazonaws.glue#JoinColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.join_column

JoinColumns: TypeAlias = list["capo_glue.types.join_column.JoinColumn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinColumns) -> list:
    import capo_glue.types.join_column

    out: list = []
    for item in value:
        out.append(capo_glue.types.join_column.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JoinColumns:
    import capo_glue.types.join_column

    out: JoinColumns = []
    for item in data:
        out.append(capo_glue.types.join_column.deserialize_aws_json_1_1(item))
    return out
