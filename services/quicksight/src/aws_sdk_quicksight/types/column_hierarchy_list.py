"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnHierarchyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_hierarchy

ColumnHierarchyList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_hierarchy.ColumnHierarchy"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnHierarchyList) -> list:
    import aws_sdk_quicksight.types.column_hierarchy

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_hierarchy.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnHierarchyList:
    import aws_sdk_quicksight.types.column_hierarchy

    out: ColumnHierarchyList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_hierarchy.deserialize_json(item))
    return out
