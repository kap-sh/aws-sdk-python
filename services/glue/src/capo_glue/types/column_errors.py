"""Generated from Smithy shape ``com.amazonaws.glue#ColumnErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_error

ColumnErrors: TypeAlias = list["capo_glue.types.column_error.ColumnError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnErrors) -> list:
    import capo_glue.types.column_error

    out: list = []
    for item in value:
        out.append(capo_glue.types.column_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnErrors:
    import capo_glue.types.column_error

    out: ColumnErrors = []
    for item in data:
        out.append(capo_glue.types.column_error.deserialize_aws_json_1_1(item))
    return out
