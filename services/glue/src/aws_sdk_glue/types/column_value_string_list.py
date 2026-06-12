"""Generated from Smithy shape ``com.amazonaws.glue#ColumnValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_values_string

ColumnValueStringList: TypeAlias = list[
    "aws_sdk_glue.types.column_values_string.ColumnValuesString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnValueStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ColumnValueStringList:
    return list(data)
