"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapDimensionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field

TreeMapDimensionFieldList: TypeAlias = list[
    "aws_sdk_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapDimensionFieldList) -> list:
    import aws_sdk_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TreeMapDimensionFieldList:
    import aws_sdk_quicksight.types.dimension_field

    out: TreeMapDimensionFieldList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.dimension_field.deserialize_json(item))
    return out
