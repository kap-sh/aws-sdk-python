"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AllowedColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_name

AllowedColumnList: TypeAlias = list["capo_cleanrooms.types.column_name.ColumnName"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedColumnList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedColumnList:
    return list(data)
