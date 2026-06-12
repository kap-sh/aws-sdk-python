"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.suggest_additional_feature

SuggestAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.suggest_additional_feature.SuggestAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> SuggestAdditionalFeatureList:
    return list(data)
