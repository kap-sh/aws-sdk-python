"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.create_hls_manifest_configuration

CreateHlsManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.create_hls_manifest_configuration.CreateHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateHlsManifests) -> list:
    import aws_sdk_mediapackagev2.types.create_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.create_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateHlsManifests:
    import aws_sdk_mediapackagev2.types.create_hls_manifest_configuration

    out: CreateHlsManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.create_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
