"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchAllRelatedItemsSortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.search_all_related_items_sort

SearchAllRelatedItemsSortList: TypeAlias = list[
    "capo_connectcases.types.search_all_related_items_sort.SearchAllRelatedItemsSort"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchAllRelatedItemsSortList) -> list:
    import capo_connectcases.types.search_all_related_items_sort

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.search_all_related_items_sort.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchAllRelatedItemsSortList:
    import capo_connectcases.types.search_all_related_items_sort

    out: SearchAllRelatedItemsSortList = []
    for item in data:
        out.append(
            capo_connectcases.types.search_all_related_items_sort.deserialize_json(item)
        )
    return out
