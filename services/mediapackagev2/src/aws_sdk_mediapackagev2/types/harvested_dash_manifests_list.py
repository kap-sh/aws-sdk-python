"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#HarvestedDashManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.harvested_dash_manifest

HarvestedDashManifestsList: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.harvested_dash_manifest.HarvestedDashManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: HarvestedDashManifestsList) -> list:
    import aws_sdk_mediapackagev2.types.harvested_dash_manifest

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_dash_manifest.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HarvestedDashManifestsList:
    import aws_sdk_mediapackagev2.types.harvested_dash_manifest

    out: HarvestedDashManifestsList = []
    for item in data:
        out.append(
            aws_sdk_mediapackagev2.types.harvested_dash_manifest.deserialize_json(item)
        )
    return out
