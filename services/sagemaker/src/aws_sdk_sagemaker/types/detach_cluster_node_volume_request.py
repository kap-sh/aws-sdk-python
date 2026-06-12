"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetachClusterNodeVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.cluster_node_id
    import aws_sdk_sagemaker.types.volume_id


class DetachClusterNodeVolumeRequest(TypedDict):
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p> The Amazon Resource Name (ARN) of your SageMaker HyperPod cluster containing the target node. Your cluster must use EKS as the orchestration and be in the <code>InService</code> state. </p>"""
    node_id: NotRequired["aws_sdk_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p> The unique identifier of the cluster node from which you want to detach the volume. </p>"""
    volume_id: NotRequired["aws_sdk_sagemaker.types.volume_id.VolumeId"]
    """<p> The unique identifier of your EBS volume that you want to detach. Your volume must be currently attached to the specified node. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachClusterNodeVolumeRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachClusterNodeVolumeRequest:
    out: DetachClusterNodeVolumeRequest = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    return out
