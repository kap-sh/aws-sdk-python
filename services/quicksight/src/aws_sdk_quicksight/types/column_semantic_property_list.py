"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_semantic_property

ColumnSemanticPropertyList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_semantic_property.ColumnSemanticProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticPropertyList) -> list:
    import aws_sdk_quicksight.types.column_semantic_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.column_semantic_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ColumnSemanticPropertyList:
    import aws_sdk_quicksight.types.column_semantic_property

    out: ColumnSemanticPropertyList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.column_semantic_property.deserialize_json(item)
        )
    return out
