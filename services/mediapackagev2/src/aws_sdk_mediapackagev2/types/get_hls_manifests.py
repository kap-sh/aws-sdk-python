"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.get_hls_manifest_configuration

GetHlsManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.get_hls_manifest_configuration.GetHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetHlsManifests) -> list:
    import aws_sdk_mediapackagev2.types.get_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.get_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetHlsManifests:
    import aws_sdk_mediapackagev2.types.get_hls_manifest_configuration

    out: GetHlsManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.get_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
