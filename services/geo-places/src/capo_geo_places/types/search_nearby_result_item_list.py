"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_nearby_result_item

SearchNearbyResultItemList: TypeAlias = list[
    "capo_geo_places.types.search_nearby_result_item.SearchNearbyResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyResultItemList) -> list:
    import capo_geo_places.types.search_nearby_result_item

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.search_nearby_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SearchNearbyResultItemList:
    import capo_geo_places.types.search_nearby_result_item

    out: SearchNearbyResultItemList = []
    for item in data:
        out.append(
            capo_geo_places.types.search_nearby_result_item.deserialize_json(item)
        )
    return out
