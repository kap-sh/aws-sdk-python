"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfMssManifest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.mss_manifest

__listOfMssManifest: TypeAlias = list[
    "capo_mediapackage_vod.types.mss_manifest.MssManifest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMssManifest) -> list:
    import capo_mediapackage_vod.types.mss_manifest

    out: list = []
    for item in value:
        out.append(capo_mediapackage_vod.types.mss_manifest.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMssManifest:
    import capo_mediapackage_vod.types.mss_manifest

    out: __listOfMssManifest = []
    for item in data:
        out.append(capo_mediapackage_vod.types.mss_manifest.deserialize_json(item))
    return out
