"""Generated from Smithy shape ``com.amazonaws.medialive#AnywhereSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class AnywhereSettings(TypedDict, closed=True):
    channel_placement_group_id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the channel placement group for the channel."""
    cluster_id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the cluster for the channel."""


# --- restJson1 ser/de ---
def serialize_json(value: AnywhereSettings) -> dict:
    out: dict = {}
    if "channel_placement_group_id" in value:
        out["channelPlacementGroupId"] = value["channel_placement_group_id"]
    if "cluster_id" in value:
        out["clusterId"] = value["cluster_id"]
    return out


def deserialize_json(data: dict) -> AnywhereSettings:
    out: AnywhereSettings = {}  # type: ignore[typeddict-item]
    if "channelPlacementGroupId" in data:
        out["channel_placement_group_id"] = data["channelPlacementGroupId"]
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    return out
