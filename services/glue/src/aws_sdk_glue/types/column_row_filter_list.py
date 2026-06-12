"""Generated from Smithy shape ``com.amazonaws.glue#ColumnRowFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_row_filter

ColumnRowFilterList: TypeAlias = list[
    "aws_sdk_glue.types.column_row_filter.ColumnRowFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnRowFilterList) -> list:
    import aws_sdk_glue.types.column_row_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.column_row_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnRowFilterList:
    import aws_sdk_glue.types.column_row_filter

    out: ColumnRowFilterList = []
    for item in data:
        out.append(aws_sdk_glue.types.column_row_filter.deserialize_aws_json_1_1(item))
    return out
