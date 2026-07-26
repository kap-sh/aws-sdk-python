"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelPlacementGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string


class UpdateChannelPlacementGroupRequest(TypedDict, closed=True):
    channel_placement_group_id: "capo_medialive.types.__string.__string"
    """The ID of the channel placement group."""
    cluster_id: "capo_medialive.types.__string.__string"
    """The ID of the cluster."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Include this parameter only if you want to change the current name of the ChannelPlacementGroup. Specify a name that is unique in the Cluster. You can't change the name. Names are case-sensitive."""
    nodes: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """Include this parameter only if you want to change the list of Nodes that are associated with the ChannelPlacementGroup."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelPlacementGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "nodes" in value:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.serialize_json(
            value["nodes"]
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelPlacementGroupRequest:
    out: UpdateChannelPlacementGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nodes" in data:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["nodes"]
        )
    return out
