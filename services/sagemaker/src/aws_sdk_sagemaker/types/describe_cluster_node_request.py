"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeClusterNodeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.cluster_node_id
    import aws_sdk_sagemaker.types.cluster_node_logical_id


class DescribeClusterNodeRequest(TypedDict):
    cluster_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster in which the node is.</p>"""
    node_id: NotRequired["aws_sdk_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p>The ID of the SageMaker HyperPod cluster node.</p>"""
    node_logical_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    ]
    """<p>The logical identifier of the node to describe. You can specify either <code>NodeLogicalId</code> or <code>InstanceId</code>, but not both. <code>NodeLogicalId</code> can be used to describe nodes that are still being provisioned and don't yet have an <code>InstanceId</code> assigned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterNodeRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterNodeRequest:
    out: DescribeClusterNodeRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    return out
