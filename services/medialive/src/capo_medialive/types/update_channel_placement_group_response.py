"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateChannelPlacementGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__string
    import capo_medialive.types.channel_placement_group_state


class UpdateChannelPlacementGroupResponse(TypedDict, closed=True):
    arn: NotRequired["capo_medialive.types.__string.__string"]
    """The ARN of this ChannelPlacementGroup. It is automatically assigned when the ChannelPlacementGroup is created."""
    channels: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """Used in ListChannelPlacementGroupsResult"""
    cluster_id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the Cluster that the Node belongs to."""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the ChannelPlacementGroup. Unique in the AWS account. The ID is the resource-id portion of the ARN."""
    name: NotRequired["capo_medialive.types.__string.__string"]
    """The name that you specified for the ChannelPlacementGroup."""
    nodes: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """An array with one item, which is the single Node that is associated with the ChannelPlacementGroup."""
    state: NotRequired[
        "capo_medialive.types.channel_placement_group_state.ChannelPlacementGroupState"
    ]
    """The current state of the ChannelPlacementGroup."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelPlacementGroupResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "channels" in value:
        import capo_medialive.types.__list_of__string

        out["channels"] = capo_medialive.types.__list_of__string.serialize_json(
            value["channels"]
        )
    if "cluster_id" in value:
        out["clusterId"] = value["cluster_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "nodes" in value:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.serialize_json(
            value["nodes"]
        )
    if "state" in value:
        import capo_medialive.types.channel_placement_group_state

        out["state"] = (
            capo_medialive.types.channel_placement_group_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelPlacementGroupResponse:
    out: UpdateChannelPlacementGroupResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "channels" in data:
        import capo_medialive.types.__list_of__string

        out["channels"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["channels"]
        )
    if "clusterId" in data:
        out["cluster_id"] = data["clusterId"]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "nodes" in data:
        import capo_medialive.types.__list_of__string

        out["nodes"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["nodes"]
        )
    if "state" in data:
        import capo_medialive.types.channel_placement_group_state

        out["state"] = (
            capo_medialive.types.channel_placement_group_state.deserialize_json(
                data["state"]
            )
        )
    return out
