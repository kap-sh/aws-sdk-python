"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_tag

ColumnTagList: TypeAlias = list["aws_sdk_quicksight.types.column_tag.ColumnTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTagList) -> list:
    import aws_sdk_quicksight.types.column_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTagList:
    import aws_sdk_quicksight.types.column_tag

    out: ColumnTagList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_tag.deserialize_json(item))
    return out
