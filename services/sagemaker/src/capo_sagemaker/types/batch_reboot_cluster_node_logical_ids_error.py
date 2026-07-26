"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodeLogicalIdsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_reboot_cluster_nodes_error_code
    import capo_sagemaker.types.cluster_node_logical_id
    import capo_sagemaker.types.string


class BatchRebootClusterNodeLogicalIdsError(TypedDict, closed=True):
    node_logical_id: NotRequired[
        "capo_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    ]
    """<p>The logical node ID of the node that encountered an error during the reboot operation.</p>"""
    error_code: NotRequired[
        "capo_sagemaker.types.batch_reboot_cluster_nodes_error_code.BatchRebootClusterNodesErrorCode"
    ]
    """<p>The error code associated with the error encountered when rebooting a node by logical node ID.</p> <p>Possible values:</p> <ul> <li> <p> <code>InstanceIdNotFound</code>: The node does not exist in the specified cluster.</p> </li> <li> <p> <code>InvalidInstanceStatus</code>: The node is in a state that does not allow rebooting. Wait for the node to finish any ongoing changes before retrying.</p> </li> <li> <p> <code>InstanceIdInUse</code>: Another operation is already in progress for this node. Wait for the operation to complete before retrying.</p> </li> <li> <p> <code>InternalServerError</code>: An internal error occurred while processing this node.</p> </li> </ul>"""
    message: NotRequired["capo_sagemaker.types.string.String"]
    """<p>A human-readable message describing the error encountered when rebooting a node by logical node ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRebootClusterNodeLogicalIdsError) -> dict:
    out: dict = {}
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
    if "error_code" in value:
        import capo_sagemaker.types.batch_reboot_cluster_nodes_error_code

        out["ErrorCode"] = (
            capo_sagemaker.types.batch_reboot_cluster_nodes_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchRebootClusterNodeLogicalIdsError:
    out: BatchRebootClusterNodeLogicalIdsError = {}  # type: ignore[typeddict-item]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    if "ErrorCode" in data:
        import capo_sagemaker.types.batch_reboot_cluster_nodes_error_code

        out["error_code"] = (
            capo_sagemaker.types.batch_reboot_cluster_nodes_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
