"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.column

ColumnList: TypeAlias = list["capo_cleanrooms.types.column.Column"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnList) -> list:
    import capo_cleanrooms.types.column

    out: list = []
    for item in value:
        out.append(capo_cleanrooms.types.column.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnList:
    import capo_cleanrooms.types.column

    out: ColumnList = []
    for item in data:
        out.append(capo_cleanrooms.types.column.deserialize_json(item))
    return out
