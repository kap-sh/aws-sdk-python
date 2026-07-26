"""Generated from Smithy shape ``com.amazonaws.quicksight#UniqueKeyColumnNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_name

UniqueKeyColumnNameList: TypeAlias = list[
    "capo_quicksight.types.column_name.ColumnName"
]


# --- restJson1 ser/de ---
def serialize_json(value: UniqueKeyColumnNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> UniqueKeyColumnNameList:
    return list(data)
