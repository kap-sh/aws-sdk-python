"""Generated from Smithy shape ``com.amazonaws.sagemaker#NodeAdditionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_availability_zones
    import aws_sdk_sagemaker.types.cluster_instance_group_name
    import aws_sdk_sagemaker.types.cluster_instance_status
    import aws_sdk_sagemaker.types.cluster_instance_types
    import aws_sdk_sagemaker.types.cluster_node_logical_id


class NodeAdditionResult(TypedDict):
    node_logical_id: (
        "aws_sdk_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    )
    """<p>A unique identifier assigned to the node that can be used to track its provisioning status through the <code>DescribeClusterNode</code> operation.</p>"""
    instance_group_name: (
        "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    )
    """<p>The name of the instance group to which the node was added.</p>"""
    status: "aws_sdk_sagemaker.types.cluster_instance_status.ClusterInstanceStatus"
    """<p>The current status of the node. Possible values include <code>Pending</code>, <code>Running</code>, <code>Failed</code>, <code>ShuttingDown</code>, <code>SystemUpdating</code>, <code>DeepHealthCheckInProgress</code>, and <code>NotFound</code>.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_sagemaker.types.cluster_availability_zones.ClusterAvailabilityZones"
    ]
    """<p>The availability zones associated with the successfully added node.</p>"""
    instance_types: NotRequired[
        "aws_sdk_sagemaker.types.cluster_instance_types.ClusterInstanceTypes"
    ]
    """<p>The instance types associated with the successfully added node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAdditionResult) -> dict:
    out: dict = {}
    out["NodeLogicalId"] = value["node_logical_id"]
    out["InstanceGroupName"] = value["instance_group_name"]
    import aws_sdk_sagemaker.types.cluster_instance_status

    out["Status"] = (
        aws_sdk_sagemaker.types.cluster_instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "availability_zones" in value:
        import aws_sdk_sagemaker.types.cluster_availability_zones

        out["AvailabilityZones"] = (
            aws_sdk_sagemaker.types.cluster_availability_zones.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "instance_types" in value:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["InstanceTypes"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.serialize_aws_json_1_1(
                value["instance_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeAdditionResult:
    out: NodeAdditionResult = {}  # type: ignore[typeddict-item]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    else:
        raise DeserializationError("NodeAdditionResult.node_logical_id required")
    if "InstanceGroupName" in data:
        out["instance_group_name"] = data["InstanceGroupName"]
    else:
        raise DeserializationError("NodeAdditionResult.instance_group_name required")
    if "Status" in data:
        import aws_sdk_sagemaker.types.cluster_instance_status

        out["status"] = (
            aws_sdk_sagemaker.types.cluster_instance_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("NodeAdditionResult.status required")
    if "AvailabilityZones" in data:
        import aws_sdk_sagemaker.types.cluster_availability_zones

        out["availability_zones"] = (
            aws_sdk_sagemaker.types.cluster_availability_zones.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if "InstanceTypes" in data:
        import aws_sdk_sagemaker.types.cluster_instance_types

        out["instance_types"] = (
            aws_sdk_sagemaker.types.cluster_instance_types.deserialize_aws_json_1_1(
                data["InstanceTypes"]
            )
        )
    return out
