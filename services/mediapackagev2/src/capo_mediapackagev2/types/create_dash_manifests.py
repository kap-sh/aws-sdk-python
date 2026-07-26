"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateDashManifests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.create_dash_manifest_configuration

CreateDashManifests: TypeAlias = list[
    "capo_mediapackagev2.types.create_dash_manifest_configuration.CreateDashManifestConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDashManifests) -> list:
    import capo_mediapackagev2.types.create_dash_manifest_configuration

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.create_dash_manifest_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CreateDashManifests:
    import capo_mediapackagev2.types.create_dash_manifest_configuration

    out: CreateDashManifests = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.create_dash_manifest_configuration.deserialize_json(
                item
            )
        )
    return out
