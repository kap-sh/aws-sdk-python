"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_search_filter

DataSourceSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.data_source_search_filter.DataSourceSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceSearchFilterList) -> list:
    import capo_quicksight.types.data_source_search_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_source_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceSearchFilterList:
    import capo_quicksight.types.data_source_search_filter

    out: DataSourceSearchFilterList = []
    for item in data:
        out.append(
            capo_quicksight.types.data_source_search_filter.deserialize_json(item)
        )
    return out
