"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list
    import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list
    import aws_sdk_sagemaker.types.cluster_node_ids
    import aws_sdk_sagemaker.types.cluster_node_logical_id_list


class BatchDeleteClusterNodesResponse(TypedDict, closed=True):
    failed: NotRequired[
        "aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list.BatchDeleteClusterNodesErrorList"
    ]
    """<p>A list of errors encountered when deleting the specified nodes.</p>"""
    successful: NotRequired["aws_sdk_sagemaker.types.cluster_node_ids.ClusterNodeIds"]
    """<p>A list of node IDs that were successfully deleted from the specified cluster.</p>"""
    failed_node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list.BatchDeleteClusterNodeLogicalIdsErrorList"
    ]
    """<p>A list of <code>NodeLogicalIds</code> that could not be deleted, along with error information explaining why the deletion failed.</p>"""
    successful_node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id_list.ClusterNodeLogicalIdList"
    ]
    """<p>A list of <code>NodeLogicalIds</code> that were successfully deleted from the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodesResponse) -> dict:
    out: dict = {}
    if "failed" in value:
        import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list

        out["Failed"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list.serialize_aws_json_1_1(
                value["failed"]
            )
        )
    if "successful" in value:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["Successful"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.serialize_aws_json_1_1(
                value["successful"]
            )
        )
    if "failed_node_logical_ids" in value:
        import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list

        out["FailedNodeLogicalIds"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list.serialize_aws_json_1_1(
                value["failed_node_logical_ids"]
            )
        )
    if "successful_node_logical_ids" in value:
        import aws_sdk_sagemaker.types.cluster_node_logical_id_list

        out["SuccessfulNodeLogicalIds"] = (
            aws_sdk_sagemaker.types.cluster_node_logical_id_list.serialize_aws_json_1_1(
                value["successful_node_logical_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteClusterNodesResponse:
    out: BatchDeleteClusterNodesResponse = {}  # type: ignore[typeddict-item]
    if "Failed" in data:
        import aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list

        out["failed"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_nodes_error_list.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    if "Successful" in data:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["successful"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    if "FailedNodeLogicalIds" in data:
        import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list

        out["failed_node_logical_ids"] = (
            aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error_list.deserialize_aws_json_1_1(
                data["FailedNodeLogicalIds"]
            )
        )
    if "SuccessfulNodeLogicalIds" in data:
        import aws_sdk_sagemaker.types.cluster_node_logical_id_list

        out["successful_node_logical_ids"] = (
            aws_sdk_sagemaker.types.cluster_node_logical_id_list.deserialize_aws_json_1_1(
                data["SuccessfulNodeLogicalIds"]
            )
        )
    return out
