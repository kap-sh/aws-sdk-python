"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHlsImageBasedTrickPlayVariant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.hls_image_based_trick_play_variant

__listOfHlsImageBasedTrickPlayVariant: TypeAlias = list[
    "capo_mediaconvert.types.hls_image_based_trick_play_variant.HlsImageBasedTrickPlayVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsImageBasedTrickPlayVariant) -> list:
    import capo_mediaconvert.types.hls_image_based_trick_play_variant

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.hls_image_based_trick_play_variant.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfHlsImageBasedTrickPlayVariant:
    import capo_mediaconvert.types.hls_image_based_trick_play_variant

    out: __listOfHlsImageBasedTrickPlayVariant = []
    for item in data:
        out.append(
            capo_mediaconvert.types.hls_image_based_trick_play_variant.deserialize_json(
                item
            )
        )
    return out
