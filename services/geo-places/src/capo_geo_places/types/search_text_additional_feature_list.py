"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchTextAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.search_text_additional_feature

SearchTextAdditionalFeatureList: TypeAlias = list[
    "capo_geo_places.types.search_text_additional_feature.SearchTextAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchTextAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchTextAdditionalFeatureList:
    return list(data)
