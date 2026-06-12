"""Generated from Smithy shape ``com.amazonaws.medialive#ListChannelPlacementGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary
    import aws_sdk_medialive.types.__string


class ListChannelPlacementGroupsResponse(TypedDict):
    channel_placement_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary.__listOfDescribeChannelPlacementGroupSummary"
    ]
    """An array of ChannelPlacementGroups that exist in the Cluster."""
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token for the next result."""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelPlacementGroupsResponse) -> dict:
    out: dict = {}
    if "channel_placement_groups" in value:
        import aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary

        out["channelPlacementGroups"] = (
            aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary.serialize_json(
                value["channel_placement_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelPlacementGroupsResponse:
    out: ListChannelPlacementGroupsResponse = {}  # type: ignore[typeddict-item]
    if "channelPlacementGroups" in data:
        import aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary

        out["channel_placement_groups"] = (
            aws_sdk_medialive.types.__list_of_describe_channel_placement_group_summary.deserialize_json(
                data["channelPlacementGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
