"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfDashAdditionalManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.dash_additional_manifest

__listOfDashAdditionalManifest: TypeAlias = list[
    "capo_mediaconvert.types.dash_additional_manifest.DashAdditionalManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashAdditionalManifest) -> list:
    import capo_mediaconvert.types.dash_additional_manifest

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.dash_additional_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfDashAdditionalManifest:
    import capo_mediaconvert.types.dash_additional_manifest

    out: __listOfDashAdditionalManifest = []
    for item in data:
        out.append(
            capo_mediaconvert.types.dash_additional_manifest.deserialize_json(item)
        )
    return out
