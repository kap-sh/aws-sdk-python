"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListMssManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_mss_manifest_configuration

ListMssManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.list_mss_manifest_configuration.ListMssManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMssManifests) -> list:
    import aws_sdk_mediapackagev2.types.list_mss_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.list_mss_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListMssManifests:
    import aws_sdk_mediapackagev2.types.list_mss_manifest_configuration

    out: ListMssManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.list_mss_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
