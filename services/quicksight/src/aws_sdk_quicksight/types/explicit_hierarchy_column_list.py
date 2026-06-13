"""Generated from Smithy shape ``com.amazonaws.quicksight#ExplicitHierarchyColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier

ExplicitHierarchyColumnList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExplicitHierarchyColumnList) -> list:
    import aws_sdk_quicksight.types.column_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExplicitHierarchyColumnList:
    import aws_sdk_quicksight.types.column_identifier

    out: ExplicitHierarchyColumnList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_identifier.deserialize_json(item))
    return out
