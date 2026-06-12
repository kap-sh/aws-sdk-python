"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHlsImageBasedTrickPlayVariant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant

__listOfHlsImageBasedTrickPlayVariant: TypeAlias = list[
    "aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant.HlsImageBasedTrickPlayVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsImageBasedTrickPlayVariant) -> list:
    import aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfHlsImageBasedTrickPlayVariant:
    import aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant

    out: __listOfHlsImageBasedTrickPlayVariant = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.hls_image_based_trick_play_variant.deserialize_json(
                item
            )
        )
    return out
