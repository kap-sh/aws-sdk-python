"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.list_hls_manifest_configuration

ListHlsManifests: TypeAlias = list[
    "capo_mediapackagev2.types.list_hls_manifest_configuration.ListHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListHlsManifests) -> list:
    import capo_mediapackagev2.types.list_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.list_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListHlsManifests:
    import capo_mediapackagev2.types.list_hls_manifest_configuration

    out: ListHlsManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.list_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
