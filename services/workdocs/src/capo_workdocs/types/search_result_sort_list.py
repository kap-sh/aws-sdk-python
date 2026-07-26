"""Generated from Smithy shape ``com.amazonaws.workdocs#SearchResultSortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.search_sort_result

SearchResultSortList: TypeAlias = list[
    "capo_workdocs.types.search_sort_result.SearchSortResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResultSortList) -> list:
    import capo_workdocs.types.search_sort_result

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.search_sort_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchResultSortList:
    import capo_workdocs.types.search_sort_result

    out: SearchResultSortList = []
    for item in data:
        out.append(capo_workdocs.types.search_sort_result.deserialize_json(item))
    return out
