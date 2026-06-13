"""Generated from Smithy shape ``com.amazonaws.quicksight#AppendedColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.appended_column

AppendedColumnList: TypeAlias = list[
    "aws_sdk_quicksight.types.appended_column.AppendedColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppendedColumnList) -> list:
    import aws_sdk_quicksight.types.appended_column

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.appended_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> AppendedColumnList:
    import aws_sdk_quicksight.types.appended_column

    out: AppendedColumnList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.appended_column.deserialize_json(item))
    return out
