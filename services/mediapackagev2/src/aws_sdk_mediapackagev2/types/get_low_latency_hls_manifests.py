"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetLowLatencyHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration

GetLowLatencyHlsManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration.GetLowLatencyHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetLowLatencyHlsManifests) -> list:
    import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetLowLatencyHlsManifests:
    import aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration

    out: GetLowLatencyHlsManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.get_low_latency_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
