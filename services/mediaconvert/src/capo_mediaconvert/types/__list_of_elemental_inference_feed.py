"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfElementalInferenceFeed``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.elemental_inference_feed

__listOfElementalInferenceFeed: TypeAlias = list[
    "capo_mediaconvert.types.elemental_inference_feed.ElementalInferenceFeed"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfElementalInferenceFeed) -> list:
    import capo_mediaconvert.types.elemental_inference_feed

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.elemental_inference_feed.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfElementalInferenceFeed:
    import capo_mediaconvert.types.elemental_inference_feed

    out: __listOfElementalInferenceFeed = []
    for item in data:
        out.append(
            capo_mediaconvert.types.elemental_inference_feed.deserialize_json(item)
        )
    return out
