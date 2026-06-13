"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.folder_search_filter

FolderSearchFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.folder_search_filter.FolderSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderSearchFilterList) -> list:
    import aws_sdk_quicksight.types.folder_search_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.folder_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FolderSearchFilterList:
    import aws_sdk_quicksight.types.folder_search_filter

    out: FolderSearchFilterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.folder_search_filter.deserialize_json(item))
    return out
