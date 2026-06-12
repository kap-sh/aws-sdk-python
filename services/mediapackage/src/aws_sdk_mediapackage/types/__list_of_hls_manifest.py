"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfHlsManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.hls_manifest

__listOfHlsManifest: TypeAlias = list[
    "aws_sdk_mediapackage.types.hls_manifest.HlsManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHlsManifest) -> list:
    import aws_sdk_mediapackage.types.hls_manifest

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackage.types.hls_manifest.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHlsManifest:
    import aws_sdk_mediapackage.types.hls_manifest

    out: __listOfHlsManifest = []
    for item in data:
        out.append(aws_sdk_mediapackage.types.hls_manifest.deserialize_json(item))
    return out
