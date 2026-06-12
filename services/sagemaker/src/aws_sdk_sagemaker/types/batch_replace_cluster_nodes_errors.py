"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchReplaceClusterNodesErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error

BatchReplaceClusterNodesErrors: TypeAlias = list[
    "aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error.BatchReplaceClusterNodesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchReplaceClusterNodesErrors) -> list:
    import aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchReplaceClusterNodesErrors:
    import aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error

    out: BatchReplaceClusterNodesErrors = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.batch_replace_cluster_nodes_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
