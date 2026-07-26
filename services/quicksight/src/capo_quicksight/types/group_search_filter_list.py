"""Generated from Smithy shape ``com.amazonaws.quicksight#GroupSearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.group_search_filter

GroupSearchFilterList: TypeAlias = list[
    "capo_quicksight.types.group_search_filter.GroupSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupSearchFilterList) -> list:
    import capo_quicksight.types.group_search_filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.group_search_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupSearchFilterList:
    import capo_quicksight.types.group_search_filter

    out: GroupSearchFilterList = []
    for item in data:
        out.append(capo_quicksight.types.group_search_filter.deserialize_json(item))
    return out
