"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfCmafImageBasedTrickPlayVariant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant

__listOfCmafImageBasedTrickPlayVariant: TypeAlias = list[
    "aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant.CmafImageBasedTrickPlayVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCmafImageBasedTrickPlayVariant) -> list:
    import aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfCmafImageBasedTrickPlayVariant:
    import aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant

    out: __listOfCmafImageBasedTrickPlayVariant = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.cmaf_image_based_trick_play_variant.deserialize_json(
                item
            )
        )
    return out
