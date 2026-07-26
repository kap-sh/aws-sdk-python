"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetDashManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.get_dash_manifest_configuration

GetDashManifests: TypeAlias = list[
    "capo_mediapackagev2.types.get_dash_manifest_configuration.GetDashManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: GetDashManifests) -> list:
    import capo_mediapackagev2.types.get_dash_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.get_dash_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GetDashManifests:
    import capo_mediapackagev2.types.get_dash_manifest_configuration

    out: GetDashManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.get_dash_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
