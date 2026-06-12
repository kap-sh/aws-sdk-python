"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchReplaceClusterNodeLogicalIdsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error

BatchReplaceClusterNodeLogicalIdsErrors: TypeAlias = list[
    "aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error.BatchReplaceClusterNodeLogicalIdsError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchReplaceClusterNodeLogicalIdsErrors) -> list:
    import aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchReplaceClusterNodeLogicalIdsErrors:
    import aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error

    out: BatchReplaceClusterNodeLogicalIdsErrors = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.batch_replace_cluster_node_logical_ids_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
