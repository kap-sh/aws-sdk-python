"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodeLogicalIdsError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code
    import aws_sdk_sagemaker.types.cluster_node_logical_id
    import aws_sdk_sagemaker.types.string


class BatchDeleteClusterNodeLogicalIdsError(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code.BatchDeleteClusterNodesErrorCode"
    ]
    """<p>The error code associated with the failure. Possible values include <code>NodeLogicalIdNotFound</code>, <code>InvalidNodeStatus</code>, and <code>InternalError</code>.</p>"""
    message: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>A descriptive message providing additional details about the error.</p>"""
    node_logical_id: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
    ]
    """<p>The <code>NodeLogicalId</code> of the node that could not be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodeLogicalIdsError) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code

        out["Code"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "node_logical_id" in value:
        out["NodeLogicalId"] = value["node_logical_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteClusterNodeLogicalIdsError:
    out: BatchDeleteClusterNodeLogicalIdsError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code

        out["code"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_code.deserialize_aws_json_1_1(
                data["Code"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "NodeLogicalId" in data:
        out["node_logical_id"] = data["NodeLogicalId"]
    return out
