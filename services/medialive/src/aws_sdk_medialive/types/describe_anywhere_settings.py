"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeAnywhereSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeAnywhereSettings(TypedDict):
    channel_placement_group_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the channel placement group for the channel."""
    cluster_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the cluster for the channel."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnywhereSettings) -> dict:
    out: dict = {}
    if "channel_placement_group_id" in value:
        out["channelPlacementGroupId"] = value["channel_placement_group_id"]
    if "cluster_id" in value:
        out["clusterId"] = value["cluster_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnywhereSettings:
    out: DescribeAnywhereSettings = {}  # type: ignore[typeddict-item]
    if "channelPlacementGroupId" in data:
        out["channel_placement_group_id"] = data["channelPlacementGroupId"]
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    return out
