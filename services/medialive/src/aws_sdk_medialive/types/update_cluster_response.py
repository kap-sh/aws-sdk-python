"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.cluster_network_settings
    import aws_sdk_medialive.types.cluster_state
    import aws_sdk_medialive.types.cluster_type


class UpdateClusterResponse(TypedDict):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the Cluster."""
    channel_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """An array of the IDs of the Channels that are associated with this Cluster. One Channel is associated with the Cluster as follows: A Channel belongs to a ChannelPlacementGroup. A ChannelPlacementGroup is attached to a Node. A Node belongs to a Cluster."""
    cluster_type: NotRequired["aws_sdk_medialive.types.cluster_type.ClusterType"]
    """The hardware type for the Cluster"""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID of the Cluster."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The user-specified name of the Cluster."""
    network_settings: NotRequired[
        "aws_sdk_medialive.types.cluster_network_settings.ClusterNetworkSettings"
    ]
    """Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with."""
    state: NotRequired["aws_sdk_medialive.types.cluster_state.ClusterState"]
    """The current state of the Cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "channel_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["channelIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["channel_ids"]
        )
    if "cluster_type" in value:
        import aws_sdk_medialive.types.cluster_type

        out["clusterType"] = aws_sdk_medialive.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "network_settings" in value:
        import aws_sdk_medialive.types.cluster_network_settings

        out["networkSettings"] = (
            aws_sdk_medialive.types.cluster_network_settings.serialize_json(
                value["network_settings"]
            )
        )
    if "state" in value:
        import aws_sdk_medialive.types.cluster_state

        out["state"] = aws_sdk_medialive.types.cluster_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateClusterResponse:
    out: UpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "channelIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["channel_ids"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["channelIds"]
        )
    if "clusterType" in data:
        import aws_sdk_medialive.types.cluster_type

        out["cluster_type"] = aws_sdk_medialive.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "networkSettings" in data:
        import aws_sdk_medialive.types.cluster_network_settings

        out["network_settings"] = (
            aws_sdk_medialive.types.cluster_network_settings.deserialize_json(
                data["networkSettings"]
            )
        )
    if "state" in data:
        import aws_sdk_medialive.types.cluster_state

        out["state"] = aws_sdk_medialive.types.cluster_state.deserialize_json(
            data["state"]
        )
    return out
