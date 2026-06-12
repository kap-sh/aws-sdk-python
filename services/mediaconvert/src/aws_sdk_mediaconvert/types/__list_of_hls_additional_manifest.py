"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHlsAdditionalManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.hls_additional_manifest

__listOfHlsAdditionalManifest: TypeAlias = list[
    "aws_sdk_mediaconvert.types.hls_additional_manifest.HlsAdditionalManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsAdditionalManifest) -> list:
    import aws_sdk_mediaconvert.types.hls_additional_manifest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconvert.types.hls_additional_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfHlsAdditionalManifest:
    import aws_sdk_mediaconvert.types.hls_additional_manifest

    out: __listOfHlsAdditionalManifest = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.hls_additional_manifest.deserialize_json(item)
        )
    return out
