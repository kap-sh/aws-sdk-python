"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfCmafAdditionalManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.cmaf_additional_manifest

__listOfCmafAdditionalManifest: TypeAlias = list[
    "aws_sdk_mediaconvert.types.cmaf_additional_manifest.CmafAdditionalManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCmafAdditionalManifest) -> list:
    import aws_sdk_mediaconvert.types.cmaf_additional_manifest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.cmaf_additional_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCmafAdditionalManifest:
    import aws_sdk_mediaconvert.types.cmaf_additional_manifest

    out: __listOfCmafAdditionalManifest = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.cmaf_additional_manifest.deserialize_json(item)
        )
    return out
