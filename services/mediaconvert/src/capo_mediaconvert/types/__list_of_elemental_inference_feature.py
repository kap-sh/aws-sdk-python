"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfElementalInferenceFeature``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.elemental_inference_feature

__listOfElementalInferenceFeature: TypeAlias = list[
    "capo_mediaconvert.types.elemental_inference_feature.ElementalInferenceFeature"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfElementalInferenceFeature) -> list:
    import capo_mediaconvert.types.elemental_inference_feature

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.elemental_inference_feature.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfElementalInferenceFeature:
    import capo_mediaconvert.types.elemental_inference_feature

    out: __listOfElementalInferenceFeature = []
    for item in data:
        out.append(
            capo_mediaconvert.types.elemental_inference_feature.deserialize_json(item)
        )
    return out
