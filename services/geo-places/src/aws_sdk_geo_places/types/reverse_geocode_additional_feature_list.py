"""Generated from Smithy shape ``com.amazonaws.geoplaces#ReverseGeocodeAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.reverse_geocode_additional_feature

ReverseGeocodeAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.reverse_geocode_additional_feature.ReverseGeocodeAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReverseGeocodeAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReverseGeocodeAdditionalFeatureList:
    return list(data)
