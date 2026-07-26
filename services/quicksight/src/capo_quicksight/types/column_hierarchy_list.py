"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnHierarchyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_hierarchy

ColumnHierarchyList: TypeAlias = list[
    "capo_quicksight.types.column_hierarchy.ColumnHierarchy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnHierarchyList) -> list:
    import capo_quicksight.types.column_hierarchy

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_hierarchy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnHierarchyList:
    import capo_quicksight.types.column_hierarchy

    out: ColumnHierarchyList = []
    for item in data:
        out.append(capo_quicksight.types.column_hierarchy.deserialize_json(item))
    return out
