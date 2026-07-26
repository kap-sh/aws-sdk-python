"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_name

ColumnList: TypeAlias = list["capo_quicksight.types.column_name.ColumnName"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnList:
    return list(data)
