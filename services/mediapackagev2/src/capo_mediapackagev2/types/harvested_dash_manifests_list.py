"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedDashManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackagev2.types.harvested_dash_manifest

HarvestedDashManifestsList: TypeAlias = list[
    "capo_mediapackagev2.types.harvested_dash_manifest.HarvestedDashManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedDashManifestsList) -> list:
    import capo_mediapackagev2.types.harvested_dash_manifest

    out: list = []
    for item in value:
        out.append(
            capo_mediapackagev2.types.harvested_dash_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarvestedDashManifestsList:
    import capo_mediapackagev2.types.harvested_dash_manifest

    out: HarvestedDashManifestsList = []
    for item in data:
        out.append(
            capo_mediapackagev2.types.harvested_dash_manifest.deserialize_json(item)
        )
    return out
