"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListLowLatencyHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration

ListLowLatencyHlsManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration.ListLowLatencyHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListLowLatencyHlsManifests) -> list:
    import aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListLowLatencyHlsManifests:
    import aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration

    out: ListLowLatencyHlsManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.list_low_latency_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
