"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.add_cluster_node_specification_list
    import aws_sdk_sagemaker.types.cluster_name_or_arn
    import aws_sdk_sagemaker.types.string


class BatchAddClusterNodesRequest(TypedDict):
    cluster_name: "aws_sdk_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    """<p>The name of the HyperPod cluster to which you want to add nodes.</p>"""
    client_token: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 8 hours. If you retry the request with the same client token within this timeframe and the same parameters, the API returns the same set of <code>NodeLogicalIds</code> with their latest status.</p>"""
    nodes_to_add: NotRequired[
        "aws_sdk_sagemaker.types.add_cluster_node_specification_list.AddClusterNodeSpecificationList"
    ]
    """<p>A list of instance groups and the number of nodes to add to each. You can specify up to 5 instance groups in a single request, with a maximum of 50 nodes total across all instance groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAddClusterNodesRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "nodes_to_add" in value:
        import aws_sdk_sagemaker.types.add_cluster_node_specification_list

        out["NodesToAdd"] = (
            aws_sdk_sagemaker.types.add_cluster_node_specification_list.serialize_aws_json_1_1(
                value["nodes_to_add"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAddClusterNodesRequest:
    out: BatchAddClusterNodesRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("BatchAddClusterNodesRequest.cluster_name required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "NodesToAdd" in data:
        import aws_sdk_sagemaker.types.add_cluster_node_specification_list

        out["nodes_to_add"] = (
            aws_sdk_sagemaker.types.add_cluster_node_specification_list.deserialize_aws_json_1_1(
                data["NodesToAdd"]
            )
        )
    return out
