"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedHlsManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvested_hls_manifest

HarvestedHlsManifestsList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.harvested_hls_manifest.HarvestedHlsManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedHlsManifestsList) -> list:
    import aws_sdk_mediapackagev2.types.harvested_hls_manifest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_hls_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarvestedHlsManifestsList:
    import aws_sdk_mediapackagev2.types.harvested_hls_manifest

    out: HarvestedHlsManifestsList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_hls_manifest.deserialize_json(item)
        )
    return out
