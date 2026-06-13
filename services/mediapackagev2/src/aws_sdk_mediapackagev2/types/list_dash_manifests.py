"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListDashManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.list_dash_manifest_configuration

ListDashManifests: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.list_dash_manifest_configuration.ListDashManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListDashManifests) -> list:
    import aws_sdk_mediapackagev2.types.list_dash_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.list_dash_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListDashManifests:
    import aws_sdk_mediapackagev2.types.list_dash_manifest_configuration

    out: ListDashManifests = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.list_dash_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
