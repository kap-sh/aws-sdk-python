"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSchemaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_schema

ColumnSchemaList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_schema.ColumnSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSchemaList) -> list:
    import aws_sdk_quicksight.types.column_schema

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_schema.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnSchemaList:
    import aws_sdk_quicksight.types.column_schema

    out: ColumnSchemaList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_schema.deserialize_json(item))
    return out
