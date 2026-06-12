"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodeLogicalIdsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error

BatchDeleteClusterNodeLogicalIdsErrorList: TypeAlias = list[
    "aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error.BatchDeleteClusterNodeLogicalIdsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodeLogicalIdsErrorList) -> list:
    import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteClusterNodeLogicalIdsErrorList:
    import aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error

    out: BatchDeleteClusterNodeLogicalIdsErrorList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.batch_delete_cluster_node_logical_ids_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
