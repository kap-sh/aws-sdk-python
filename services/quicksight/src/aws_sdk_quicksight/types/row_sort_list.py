"""Generated from Smithy shape ``com.amazonaws.quicksight#RowSortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_sort_options

RowSortList: TypeAlias = list[
    "aws_sdk_quicksight.types.field_sort_options.FieldSortOptions"
]


# --- restJson1 ser/de ---
def serialize_json(value: RowSortList) -> list:
    import aws_sdk_quicksight.types.field_sort_options

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.field_sort_options.serialize_json(item))
    return out


def deserialize_json(data: list) -> RowSortList:
    import aws_sdk_quicksight.types.field_sort_options

    out: RowSortList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.field_sort_options.deserialize_json(item))
    return out
