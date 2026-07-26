"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateLowLatencyHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration

CreateLowLatencyHlsManifests: TypeAlias = list[
    "capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration.CreateLowLatencyHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateLowLatencyHlsManifests) -> list:
    import capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateLowLatencyHlsManifests:
    import capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration

    out: CreateLowLatencyHlsManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.create_low_latency_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
