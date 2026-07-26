"""Generated from Smithy shape ``com.amazonaws.quicksight#BodySectionDynamicDimensionSortConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_sort

BodySectionDynamicDimensionSortConfigurationList: TypeAlias = list[
    "capo_quicksight.types.column_sort.ColumnSort"
]


# --- restJson1 ser/de ---
def serialize_json(value: BodySectionDynamicDimensionSortConfigurationList) -> list:
    import capo_quicksight.types.column_sort

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_sort.serialize_json(item))
    return out


def deserialize_json(data: list) -> BodySectionDynamicDimensionSortConfigurationList:
    import capo_quicksight.types.column_sort

    out: BodySectionDynamicDimensionSortConfigurationList = []
    for item in data:
        out.append(capo_quicksight.types.column_sort.deserialize_json(item))
    return out
