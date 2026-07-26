"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_name

ColumnNameList: TypeAlias = list["capo_quicksight.types.column_name.ColumnName"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnNameList:
    return list(data)
