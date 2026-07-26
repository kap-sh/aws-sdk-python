"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfMsSmoothAdditionalManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.ms_smooth_additional_manifest

__listOfMsSmoothAdditionalManifest: TypeAlias = list[
    "capo_mediaconvert.types.ms_smooth_additional_manifest.MsSmoothAdditionalManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMsSmoothAdditionalManifest) -> list:
    import capo_mediaconvert.types.ms_smooth_additional_manifest

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.ms_smooth_additional_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMsSmoothAdditionalManifest:
    import capo_mediaconvert.types.ms_smooth_additional_manifest

    out: __listOfMsSmoothAdditionalManifest = []
    for item in data:
        out.append(
            capo_mediaconvert.types.ms_smooth_additional_manifest.deserialize_json(item)
        )
    return out
