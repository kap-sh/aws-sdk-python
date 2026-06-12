"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.cluster_node_ids
    import aws_sdk_sagemaker.types.cluster_node_logical_id_list


class BatchRebootClusterNodesRequest(TypedDict):
    cluster_name: NotRequired[
        "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the SageMaker HyperPod cluster containing the nodes to reboot.</p>"""
    node_ids: NotRequired["aws_sdk_sagemaker.types.cluster_node_ids.ClusterNodeIds"]
    """<p>A list of EC2 instance IDs to reboot using soft recovery. You can specify between 1 and 25 instance IDs.</p> <note> <ul> <li> <p>Either <code>NodeIds</code> or <code>NodeLogicalIds</code> must be provided (or both), but at least one is required.</p> </li> <li> <p>Each instance ID must follow the pattern <code>i-</code> followed by 17 hexadecimal characters (for example, <code>i-0123456789abcdef0</code>).</p> </li> </ul> </note>"""
    node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id_list.ClusterNodeLogicalIdList"
    ]
    """<p>A list of logical node IDs to reboot using soft recovery. You can specify between 1 and 25 logical node IDs.</p> <p>The <code>NodeLogicalId</code> is a unique identifier that persists throughout the node's lifecycle and can be used to track nodes that are still being provisioned and don't yet have an EC2 instance ID assigned.</p> <important> <ul> <li> <p>This parameter is only supported for clusters using <code>Continuous</code> as the <code>NodeProvisioningMode</code>. For clusters using the default provisioning mode, use <code>NodeIds</code> instead.</p> </li> <li> <p>Either <code>NodeIds</code> or <code>NodeLogicalIds</code> must be provided (or both), but at least one is required.</p> </li> </ul> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRebootClusterNodesRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> BatchRebootClusterNodesRequest:
    out: BatchRebootClusterNodesRequest = {}  # type: ignore[typeddict-item]
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
