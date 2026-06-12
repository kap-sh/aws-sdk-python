"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfDashManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.dash_manifest

__listOfDashManifest: TypeAlias = list[
    "aws_sdk_mediapackage_vod.types.dash_manifest.DashManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashManifest) -> list:
    import aws_sdk_mediapackage_vod.types.dash_manifest

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackage_vod.types.dash_manifest.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDashManifest:
    import aws_sdk_mediapackage_vod.types.dash_manifest

    out: __listOfDashManifest = []
    for item in data:
        out.append(aws_sdk_mediapackage_vod.types.dash_manifest.deserialize_json(item))
    return out
