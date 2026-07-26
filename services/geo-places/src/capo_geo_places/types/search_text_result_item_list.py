"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_text_result_item

SearchTextResultItemList: TypeAlias = list[
    "capo_geo_places.types.search_text_result_item.SearchTextResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextResultItemList) -> list:
    import capo_geo_places.types.search_text_result_item

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.search_text_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchTextResultItemList:
    import capo_geo_places.types.search_text_result_item

    out: SearchTextResultItemList = []
    for item in data:
        out.append(capo_geo_places.types.search_text_result_item.deserialize_json(item))
    return out
