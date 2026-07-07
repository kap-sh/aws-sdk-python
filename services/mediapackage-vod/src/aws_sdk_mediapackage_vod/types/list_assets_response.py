"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListAssetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__list_of_asset_shallow
    import aws_sdk_mediapackage_vod.types.__string


class ListAssetsResponse(TypedDict, closed=True):
    assets: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of_asset_shallow.__listOfAssetShallow"
    ]
    """A list of MediaPackage VOD Asset resources."""
    next_token: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetsResponse) -> dict:
    out: dict = {}
    if "assets" in value:
        import aws_sdk_mediapackage_vod.types.__list_of_asset_shallow

        out["assets"] = (
            aws_sdk_mediapackage_vod.types.__list_of_asset_shallow.serialize_json(
                value["assets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetsResponse:
    out: ListAssetsResponse = {}  # type: ignore[typeddict-item]
    if "assets" in data:
        import aws_sdk_mediapackage_vod.types.__list_of_asset_shallow

        out["assets"] = (
            aws_sdk_mediapackage_vod.types.__list_of_asset_shallow.deserialize_json(
                data["assets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
