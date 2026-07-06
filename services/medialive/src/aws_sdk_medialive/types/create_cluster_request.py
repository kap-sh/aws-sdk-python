"""Generated from Smithy shape ``com.amazonaws.medialive#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.cluster_network_settings_create_request
    import aws_sdk_medialive.types.cluster_type
    import aws_sdk_medialive.types.tags


class CreateClusterRequest(TypedDict, closed=True):
    cluster_type: NotRequired["aws_sdk_medialive.types.cluster_type.ClusterType"]
    """Specify a type. All the Nodes that you later add to this Cluster must be this type of hardware. One Cluster instance can't contain different hardware types. You won't be able to change this parameter after you create the Cluster."""
    instance_role_arn: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ARN of the IAM role for the Node in this Cluster. The role must include all the operations that you expect these Node to perform. If necessary, create a role in IAM, then attach it here."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specify a name that is unique in the AWS account. We recommend that you assign a name that hints at the types of Nodes in the Cluster. Names are case-sensitive."""
    network_settings: NotRequired[
        "aws_sdk_medialive.types.cluster_network_settings_create_request.ClusterNetworkSettingsCreateRequest"
    ]
    """Network settings that connect the Nodes in the Cluster to one or more of the Networks that the Cluster is associated with."""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The unique ID of the request."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "cluster_type" in value:
        import aws_sdk_medialive.types.cluster_type

        out["clusterType"] = aws_sdk_medialive.types.cluster_type.serialize_json(
            value["cluster_type"]
        )
    if "instance_role_arn" in value:
        out["instanceRoleArn"] = value["instance_role_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "network_settings" in value:
        import aws_sdk_medialive.types.cluster_network_settings_create_request

        out["networkSettings"] = (
            aws_sdk_medialive.types.cluster_network_settings_create_request.serialize_json(
                value["network_settings"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if "clusterType" in data:
        import aws_sdk_medialive.types.cluster_type

        out["cluster_type"] = aws_sdk_medialive.types.cluster_type.deserialize_json(
            data["clusterType"]
        )
    if "instanceRoleArn" in data:
        out["instance_role_arn"] = data["instanceRoleArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "networkSettings" in data:
        import aws_sdk_medialive.types.cluster_network_settings_create_request

        out["network_settings"] = (
            aws_sdk_medialive.types.cluster_network_settings_create_request.deserialize_json(
                data["networkSettings"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
