"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTagNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_tag_name

ColumnTagNames: TypeAlias = list["capo_quicksight.types.column_tag_name.ColumnTagName"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTagNames) -> list:
    import capo_quicksight.types.column_tag_name

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_tag_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnTagNames:
    import capo_quicksight.types.column_tag_name

    out: ColumnTagNames = []
    for item in data:
        out.append(capo_quicksight.types.column_tag_name.deserialize_json(item))
    return out
