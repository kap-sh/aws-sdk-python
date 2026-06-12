"""Generated from Smithy shape ``com.amazonaws.finspacedata#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.column_definition

ColumnList: TypeAlias = list[
    "aws_sdk_finspace_data.types.column_definition.ColumnDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnList) -> list:
    import aws_sdk_finspace_data.types.column_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace_data.types.column_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnList:
    import aws_sdk_finspace_data.types.column_definition

    out: ColumnList = []
    for item in data:
        out.append(aws_sdk_finspace_data.types.column_definition.deserialize_json(item))
    return out
