"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedLowLatencyHlsManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest

HarvestedLowLatencyHlsManifestsList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest.HarvestedLowLatencyHlsManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedLowLatencyHlsManifestsList) -> list:
    import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarvestedLowLatencyHlsManifestsList:
    import aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest

    out: HarvestedLowLatencyHlsManifestsList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_low_latency_hls_manifest.deserialize_json(
                item
            )
        )
    return out
