"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotGroupByColumnNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_name

PivotGroupByColumnNameList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_name.ColumnName"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotGroupByColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> PivotGroupByColumnNameList:
    return list(data)
