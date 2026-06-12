"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.search_nearby_result_item

SearchNearbyResultItemList: TypeAlias = list[
    "aws_sdk_geo_places.types.search_nearby_result_item.SearchNearbyResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyResultItemList) -> list:
    import aws_sdk_geo_places.types.search_nearby_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_places.types.search_nearby_result_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchNearbyResultItemList:
    import aws_sdk_geo_places.types.search_nearby_result_item

    out: SearchNearbyResultItemList = []
    for item in data:
        out.append(
            aws_sdk_geo_places.types.search_nearby_result_item.deserialize_json(item)
        )
    return out
