"""Generated from Smithy shape ``com.amazonaws.quicksight#PredefinedHierarchyColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier

PredefinedHierarchyColumnList: TypeAlias = list[
    "capo_quicksight.types.column_identifier.ColumnIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: PredefinedHierarchyColumnList) -> list:
    import capo_quicksight.types.column_identifier

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> PredefinedHierarchyColumnList:
    import capo_quicksight.types.column_identifier

    out: PredefinedHierarchyColumnList = []
    for item in data:
        out.append(capo_quicksight.types.column_identifier.deserialize_json(item))
    return out
