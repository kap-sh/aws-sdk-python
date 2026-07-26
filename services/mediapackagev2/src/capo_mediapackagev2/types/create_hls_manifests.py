"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateHlsManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.create_hls_manifest_configuration

CreateHlsManifests: TypeAlias = list[
    "capo_mediapackagev2.types.create_hls_manifest_configuration.CreateHlsManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateHlsManifests) -> list:
    import capo_mediapackagev2.types.create_hls_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.create_hls_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateHlsManifests:
    import capo_mediapackagev2.types.create_hls_manifest_configuration

    out: CreateHlsManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.create_hls_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
