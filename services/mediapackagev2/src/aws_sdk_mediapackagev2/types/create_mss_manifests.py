"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateMssManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.create_mss_manifest_configuration

CreateMssManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.create_mss_manifest_configuration.CreateMssManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMssManifests) -> list:
    import aws_sdk_mediapackagev2.types.create_mss_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.create_mss_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateMssManifests:
    import aws_sdk_mediapackagev2.types.create_mss_manifest_configuration

    out: CreateMssManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.create_mss_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
