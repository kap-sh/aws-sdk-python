"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_group

ColumnGroupList: TypeAlias = list["aws_sdk_quicksight.types.column_group.ColumnGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupList) -> list:
    import aws_sdk_quicksight.types.column_group

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnGroupList:
    import aws_sdk_quicksight.types.column_group

    out: ColumnGroupList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_group.deserialize_json(item))
    return out
