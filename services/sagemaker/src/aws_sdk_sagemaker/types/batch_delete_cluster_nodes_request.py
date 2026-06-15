"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.cluster_node_ids
    import aws_sdk_sagemaker.types.cluster_node_logical_id_list


class BatchDeleteClusterNodesRequest(TypedDict):
    cluster_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name of the SageMaker HyperPod cluster from which to delete the specified nodes.</p>"""
    node_ids: NotRequired["aws_sdk_sagemaker.types.cluster_node_ids.ClusterNodeIds"]
    r"""<p>A list of node IDs to be deleted from the specified cluster.</p> <note> <ul> <li> <p>For SageMaker HyperPod clusters using the Slurm workload manager, you cannot remove instances that are configured as Slurm controller nodes.</p> </li> <li> <p>If you need to delete more than 99 instances, contact <a href=\"http://aws.amazon.com/contact-us/\">Support</a> for assistance.</p> </li> </ul> </note>"""
    node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id_list.ClusterNodeLogicalIdList"
    ]
    """<p>A list of <code>NodeLogicalIds</code> identifying the nodes to be deleted. You can specify up to 50 <code>NodeLogicalIds</code>. You must specify either <code>NodeLogicalIds</code>, <code>InstanceIds</code>, or both, with a combined maximum of 50 identifiers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodesRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "node_ids" in value:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["NodeIds"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.serialize_aws_json_1_1(
                value["node_ids"]
            )
        )
    if "node_logical_ids" in value:
        import aws_sdk_sagemaker.types.cluster_node_logical_id_list

        out["NodeLogicalIds"] = (
            aws_sdk_sagemaker.types.cluster_node_logical_id_list.serialize_aws_json_1_1(
                value["node_logical_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteClusterNodesRequest:
    out: BatchDeleteClusterNodesRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "NodeIds" in data:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["node_ids"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.deserialize_aws_json_1_1(
                data["NodeIds"]
            )
        )
    if "NodeLogicalIds" in data:
        import aws_sdk_sagemaker.types.cluster_node_logical_id_list

        out["node_logical_ids"] = (
            aws_sdk_sagemaker.types.cluster_node_logical_id_list.deserialize_aws_json_1_1(
                data["NodeLogicalIds"]
            )
        )
    return out
