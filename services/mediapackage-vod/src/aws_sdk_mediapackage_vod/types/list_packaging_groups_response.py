"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#ListPackagingGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.__list_of_packaging_group
    import aws_sdk_mediapackage_vod.types.__string


class ListPackagingGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mediapackage_vod.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""
    packaging_groups: NotRequired[
        "aws_sdk_mediapackage_vod.types.__list_of_packaging_group.__listOfPackagingGroup"
    ]
    """A list of MediaPackage VOD PackagingGroup resources."""


# --- restJson1 ser/de ---
def serialize_json(value: ListPackagingGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "packaging_groups" in value:
        import aws_sdk_mediapackage_vod.types.__list_of_packaging_group

        out["packagingGroups"] = (
            aws_sdk_mediapackage_vod.types.__list_of_packaging_group.serialize_json(
                value["packaging_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListPackagingGroupsResponse:
    out: ListPackagingGroupsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "packagingGroups" in data:
        import aws_sdk_mediapackage_vod.types.__list_of_packaging_group

        out["packaging_groups"] = (
            aws_sdk_mediapackage_vod.types.__list_of_packaging_group.deserialize_json(
                data["packagingGroups"]
            )
        )
    return out
