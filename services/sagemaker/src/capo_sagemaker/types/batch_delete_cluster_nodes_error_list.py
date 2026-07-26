"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDeleteClusterNodesErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_delete_cluster_nodes_error

BatchDeleteClusterNodesErrorList: TypeAlias = list[
    "capo_sagemaker.types.batch_delete_cluster_nodes_error.BatchDeleteClusterNodesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteClusterNodesErrorList) -> list:
    import capo_sagemaker.types.batch_delete_cluster_nodes_error

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.batch_delete_cluster_nodes_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchDeleteClusterNodesErrorList:
    import capo_sagemaker.types.batch_delete_cluster_nodes_error

    out: BatchDeleteClusterNodesErrorList = []
    for item in data:
        out.append(
            capo_sagemaker.types.batch_delete_cluster_nodes_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
