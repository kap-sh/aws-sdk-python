"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_tag

ColumnTagList: TypeAlias = list["capo_quicksight.types.column_tag.ColumnTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTagList) -> list:
    import capo_quicksight.types.column_tag

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTagList:
    import capo_quicksight.types.column_tag

    out: ColumnTagList = []
    for item in data:
        out.append(capo_quicksight.types.column_tag.deserialize_json(item))
    return out
