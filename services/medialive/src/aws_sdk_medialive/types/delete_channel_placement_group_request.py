"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteChannelPlacementGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteChannelPlacementGroupRequest(TypedDict):
    channel_placement_group_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the channel placement group."""
    cluster_id: "aws_sdk_medialive.types.__string.__string"
    """The ID of the cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelPlacementGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelPlacementGroupRequest:
    out: DeleteChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
    return out
