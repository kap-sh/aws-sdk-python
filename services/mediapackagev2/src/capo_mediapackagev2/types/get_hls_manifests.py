"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.get_hls_manifest_configuration

GetHlsManifests: TypeAlias = list[
    "capo_mediapackagev2.types.get_hls_manifest_configuration.GetHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetHlsManifests) -> list:
    import capo_mediapackagev2.types.get_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.get_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetHlsManifests:
    import capo_mediapackagev2.types.get_hls_manifest_configuration

    out: GetHlsManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.get_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
