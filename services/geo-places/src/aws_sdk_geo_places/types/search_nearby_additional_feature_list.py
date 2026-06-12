"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.search_nearby_additional_feature

SearchNearbyAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.search_nearby_additional_feature.SearchNearbyAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchNearbyAdditionalFeatureList:
    return list(data)
