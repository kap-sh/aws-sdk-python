"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetMssManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.get_mss_manifest_configuration

GetMssManifests: TypeAlias = list[
    "capo_mediapackagev2.types.get_mss_manifest_configuration.GetMssManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetMssManifests) -> list:
    import capo_mediapackagev2.types.get_mss_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.get_mss_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetMssManifests:
    import capo_mediapackagev2.types.get_mss_manifest_configuration

    out: GetMssManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.get_mss_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
