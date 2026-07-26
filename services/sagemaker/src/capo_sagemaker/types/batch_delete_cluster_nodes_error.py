"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_delete_cluster_nodes_error_code
    import capo_sagemaker.types.cluster_node_id


class BatchDeleteClusterNodesError(TypedDict, closed=True):
    code: NotRequired[
        "capo_sagemaker.types.batch_delete_cluster_nodes_error_code.BatchDeleteClusterNodesErrorCode"
    ]
    """<p>The error code associated with the error encountered when deleting a node.</p> <p>The code provides information about the specific issue encountered, such as the node not being found, the node's status being invalid for deletion, or the node ID being in use by another process.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the error encountered when deleting a node.</p>"""
    node_id: NotRequired["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p>The ID of the node that encountered an error during the deletion process.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodesError) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_sagemaker.types.batch_delete_cluster_nodes_error_code

        out["Code"] = (
            capo_sagemaker.types.batch_delete_cluster_nodes_error_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteClusterNodesError:
    out: BatchDeleteClusterNodesError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_sagemaker.types.batch_delete_cluster_nodes_error_code

        out["code"] = (
            capo_sagemaker.types.batch_delete_cluster_nodes_error_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    return out
