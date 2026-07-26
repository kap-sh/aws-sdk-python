"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfAssetShallow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediapackage_vod.types.asset_shallow

__listOfAssetShallow: TypeAlias = list[
    "capo_mediapackage_vod.types.asset_shallow.AssetShallow"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAssetShallow) -> list:
    import capo_mediapackage_vod.types.asset_shallow

    out: list = []
    for item in value:
        out.append(capo_mediapackage_vod.types.asset_shallow.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAssetShallow:
    import capo_mediapackage_vod.types.asset_shallow

    out: __listOfAssetShallow = []
    for item in data:
        out.append(capo_mediapackage_vod.types.asset_shallow.deserialize_json(item))
    return out
