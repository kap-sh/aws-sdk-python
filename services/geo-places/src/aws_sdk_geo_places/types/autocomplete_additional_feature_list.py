"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteAdditionalFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.autocomplete_additional_feature

AutocompleteAdditionalFeatureList: TypeAlias = list[
    "aws_sdk_geo_places.types.autocomplete_additional_feature.AutocompleteAdditionalFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteAdditionalFeatureList) -> list:
    return list(value)


def deserialize_json(data: list) -> AutocompleteAdditionalFeatureList:
    return list(data)
