"""Generated from Smithy shape ``com.amazonaws.quicksight#FilledMapDimensionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field

FilledMapDimensionFieldList: TypeAlias = list[
    "aws_sdk_quicksight.types.dimension_field.DimensionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilledMapDimensionFieldList) -> list:
    import aws_sdk_quicksight.types.dimension_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.dimension_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilledMapDimensionFieldList:
    import aws_sdk_quicksight.types.dimension_field

    out: FilledMapDimensionFieldList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.dimension_field.deserialize_json(item))
    return out
