"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfDashIsoImageBasedTrickPlayVariant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant

__listOfDashIsoImageBasedTrickPlayVariant: TypeAlias = list[
    "aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant.DashIsoImageBasedTrickPlayVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashIsoImageBasedTrickPlayVariant) -> list:
    import aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDashIsoImageBasedTrickPlayVariant:
    import aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant

    out: __listOfDashIsoImageBasedTrickPlayVariant = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.dash_iso_image_based_trick_play_variant.deserialize_json(
                item
            )
        )
    return out
