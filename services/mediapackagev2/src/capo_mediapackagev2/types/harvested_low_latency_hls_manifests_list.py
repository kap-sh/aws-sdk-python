"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedLowLatencyHlsManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.harvested_low_latency_hls_manifest

HarvestedLowLatencyHlsManifestsList: TypeAlias = list[
    "capo_mediapackagev2.types.harvested_low_latency_hls_manifest.HarvestedLowLatencyHlsManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedLowLatencyHlsManifestsList) -> list:
    import capo_mediapackagev2.types.harvested_low_latency_hls_manifest

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.harvested_low_latency_hls_manifest.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HarvestedLowLatencyHlsManifestsList:
    import capo_mediapackagev2.types.harvested_low_latency_hls_manifest

    out: HarvestedLowLatencyHlsManifestsList = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.harvested_low_latency_hls_manifest.deserialize_json(
                item
            )
        )
    return out
