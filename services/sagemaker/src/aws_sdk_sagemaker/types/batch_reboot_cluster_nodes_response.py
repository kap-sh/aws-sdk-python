"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors
    import aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors
    import aws_sdk_sagemaker.types.cluster_node_ids
    import aws_sdk_sagemaker.types.cluster_node_logical_id_list


class BatchRebootClusterNodesResponse(TypedDict):
    successful: NotRequired["aws_sdk_sagemaker.types.cluster_node_ids.ClusterNodeIds"]
    """<p>A list of EC2 instance IDs for which the reboot operation was successfully initiated.</p>"""
    failed: NotRequired[
        "aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors.BatchRebootClusterNodesErrors"
    ]
    """<p>A list of errors encountered for EC2 instance IDs that could not be rebooted. Each error includes the instance ID, an error code, and a descriptive message.</p>"""
    failed_node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors.BatchRebootClusterNodeLogicalIdsErrors"
    ]
    """<p>A list of errors encountered for logical node IDs that could not be rebooted. Each error includes the logical node ID, an error code, and a descriptive message. This field is only present when <code>NodeLogicalIds</code> were provided in the request.</p>"""
    successful_node_logical_ids: NotRequired[
        "aws_sdk_sagemaker.types.cluster_node_logical_id_list.ClusterNodeLogicalIdList"
    ]
    """<p>A list of logical node IDs for which the reboot operation was successfully initiated. This field is only present when <code>NodeLogicalIds</code> were provided in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRebootClusterNodesResponse) -> dict:
    out: dict = {}
    if "successful" in value:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["Successful"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.serialize_aws_json_1_1(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors

        out["Failed"] = (
            aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors.serialize_aws_json_1_1(
                value["failed"]
            )
        )
    if "failed_node_logical_ids" in value:
        import aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors

        out["FailedNodeLogicalIds"] = (
            aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> BatchRebootClusterNodesResponse:
    out: BatchRebootClusterNodesResponse = {}  # type: ignore[typeddict-item]
    if "Successful" in data:
        import aws_sdk_sagemaker.types.cluster_node_ids

        out["successful"] = (
            aws_sdk_sagemaker.types.cluster_node_ids.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    if "Failed" in data:
        import aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors

        out["failed"] = (
            aws_sdk_sagemaker.types.batch_reboot_cluster_nodes_errors.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    if "FailedNodeLogicalIds" in data:
        import aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors

        out["failed_node_logical_ids"] = (
            aws_sdk_sagemaker.types.batch_reboot_cluster_node_logical_ids_errors.deserialize_aws_json_1_1(
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
