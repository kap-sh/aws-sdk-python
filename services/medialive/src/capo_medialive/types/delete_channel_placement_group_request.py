"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteChannelPlacementGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DeleteChannelPlacementGroupRequest(TypedDict, closed=True):
    channel_placement_group_id: "capo_medialive.types.__string.__string"
    """The ID of the channel placement group."""
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelPlacementGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelPlacementGroupRequest:
    out: DeleteChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
    return out
