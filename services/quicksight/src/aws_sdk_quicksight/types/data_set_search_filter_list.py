"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_search_filter

DataSetSearchFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_search_filter.DataSetSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSearchFilterList) -> list:
    import aws_sdk_quicksight.types.data_set_search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_set_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetSearchFilterList:
    import aws_sdk_quicksight.types.data_set_search_filter

    out: DataSetSearchFilterList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_set_search_filter.deserialize_json(item)
        )
    return out
