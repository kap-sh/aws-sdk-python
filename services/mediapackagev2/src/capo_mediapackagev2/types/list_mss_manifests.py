"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListMssManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.list_mss_manifest_configuration

ListMssManifests: TypeAlias = list[
    "capo_mediapackagev2.types.list_mss_manifest_configuration.ListMssManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListMssManifests) -> list:
    import capo_mediapackagev2.types.list_mss_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.list_mss_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListMssManifests:
    import capo_mediapackagev2.types.list_mss_manifest_configuration

    out: ListMssManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.list_mss_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
