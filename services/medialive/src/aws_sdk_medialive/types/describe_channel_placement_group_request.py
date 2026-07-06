"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeChannelPlacementGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeChannelPlacementGroupRequest(TypedDict, closed=True):
    channel_placement_group_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the channel placement group."""
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChannelPlacementGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChannelPlacementGroupRequest:
    out: DescribeChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
    return out
