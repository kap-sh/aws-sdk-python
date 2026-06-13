"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionDynamicDimensionSortConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_sort

BodySectionDynamicDimensionSortConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_sort.ColumnSort"
]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionDynamicDimensionSortConfigurationList) -> list:
    import aws_sdk_quicksight.types.column_sort

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_sort.serialize_json(item))
    return out


def deserialize_json(data: list) -> BodySectionDynamicDimensionSortConfigurationList:
    import aws_sdk_quicksight.types.column_sort

    out: BodySectionDynamicDimensionSortConfigurationList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_sort.deserialize_json(item))
    return out
