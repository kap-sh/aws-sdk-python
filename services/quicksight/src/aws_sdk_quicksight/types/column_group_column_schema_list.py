"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupColumnSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_group_column_schema

ColumnGroupColumnSchemaList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_group_column_schema.ColumnGroupColumnSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupColumnSchemaList) -> list:
    import aws_sdk_quicksight.types.column_group_column_schema

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.column_group_column_schema.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnGroupColumnSchemaList:
    import aws_sdk_quicksight.types.column_group_column_schema

    out: ColumnGroupColumnSchemaList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.column_group_column_schema.deserialize_json(item)
        )
    return out
