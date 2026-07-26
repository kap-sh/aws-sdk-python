"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfDashIsoImageBasedTrickPlayVariant``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.dash_iso_image_based_trick_play_variant

__listOfDashIsoImageBasedTrickPlayVariant: TypeAlias = list[
    "capo_mediaconvert.types.dash_iso_image_based_trick_play_variant.DashIsoImageBasedTrickPlayVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashIsoImageBasedTrickPlayVariant) -> list:
    import capo_mediaconvert.types.dash_iso_image_based_trick_play_variant

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.dash_iso_image_based_trick_play_variant.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfDashIsoImageBasedTrickPlayVariant:
    import capo_mediaconvert.types.dash_iso_image_based_trick_play_variant

    out: __listOfDashIsoImageBasedTrickPlayVariant = []
    for item in data:
        out.append(
            capo_mediaconvert.types.dash_iso_image_based_trick_play_variant.deserialize_json(
                item
            )
        )
    return out
