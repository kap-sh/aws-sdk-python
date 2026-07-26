"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfCmafAdditionalManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.cmaf_additional_manifest

__listOfCmafAdditionalManifest: TypeAlias = list[
    "capo_mediaconvert.types.cmaf_additional_manifest.CmafAdditionalManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCmafAdditionalManifest) -> list:
    import capo_mediaconvert.types.cmaf_additional_manifest

    out: list = []
    for item in value:
        out.append(
            capo_mediaconvert.types.cmaf_additional_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCmafAdditionalManifest:
    import capo_mediaconvert.types.cmaf_additional_manifest

    out: __listOfCmafAdditionalManifest = []
    for item in data:
        out.append(
            capo_mediaconvert.types.cmaf_additional_manifest.deserialize_json(item)
        )
    return out
