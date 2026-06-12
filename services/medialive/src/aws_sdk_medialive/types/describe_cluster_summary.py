"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeClusterSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.cluster_network_settings
    import aws_sdk_medialive.types.cluster_state
    import aws_sdk_medialive.types.cluster_type


class DescribeClusterSummary(TypedDict):
    arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of this Cluster. It is automatically assigned when the Cluster is created."""
    channel_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """An array of the IDs of the Channels that are associated with this Cluster. One Channel is associated with the Cluster as follows: A Channel belongs to a ChannelPlacementGroup. A ChannelPlacementGroup is attached to a Node. A Node belongs to a Cluster."""
    cluster_type: NotRequired["aws_sdk_medialive.types.cluster_type.ClusterType"]
    """The hardware type for the Cluster."""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the Cluster. Unique in the AWS account. The ID is the resource-id portion of the ARN."""
    instance_role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the IAM role for the Node in this Cluster. Any Nodes that are associated with this Cluster assume this role. The role gives permissions to the operations that you expect these Node to perform."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The name that you specified for the Cluster."""
    network_settings: NotRequired[
        "aws_sdk_medialive.types.cluster_network_settings.ClusterNetworkSettings"
    ]
    """Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with."""
    state: NotRequired["aws_sdk_medialive.types.cluster_state.ClusterState"]
    """The current state of the Cluster."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClusterSummary) -> dict:
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
    if "instance_role_arn" in value:
        out["instanceRoleArn"] = value["instance_role_arn"]
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


def deserialize_json(data: dict) -> DescribeClusterSummary:
    out: DescribeClusterSummary = {}  # type: ignore[typeddict-item]
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
    if "instanceRoleArn" in data:
        out["instance_role_arn"] = data["instanceRoleArn"]
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
