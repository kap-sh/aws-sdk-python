"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.get_place_additional_feature

GetPlaceAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.get_place_additional_feature.GetPlaceAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> GetPlaceAdditionalFeatureList:
    return list(data)
