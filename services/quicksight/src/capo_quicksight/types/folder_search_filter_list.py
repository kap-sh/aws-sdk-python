"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.folder_search_filter

FolderSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.folder_search_filter.FolderSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderSearchFilterList) -> list:
    import capo_quicksight.types.folder_search_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.folder_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderSearchFilterList:
    import capo_quicksight.types.folder_search_filter

    out: FolderSearchFilterList = []
    for item in data:
        out.append(capo_quicksight.types.folder_search_filter.deserialize_json(item))
    return out
