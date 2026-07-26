"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_group

ColumnGroupList: TypeAlias = list["capo_quicksight.types.column_group.ColumnGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroupList) -> list:
    import capo_quicksight.types.column_group

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnGroupList:
    import capo_quicksight.types.column_group

    out: ColumnGroupList = []
    for item in data:
        out.append(capo_quicksight.types.column_group.deserialize_json(item))
    return out
