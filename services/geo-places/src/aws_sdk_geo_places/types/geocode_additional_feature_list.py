"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.geocode_additional_feature

GeocodeAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.geocode_additional_feature.GeocodeAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> GeocodeAdditionalFeatureList:
    return list(data)
