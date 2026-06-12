"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchAddClusterNodesErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.batch_add_cluster_nodes_error

BatchAddClusterNodesErrorList: TypeAlias = list[
    "aws_sdk_sagemaker.types.batch_add_cluster_nodes_error.BatchAddClusterNodesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAddClusterNodesErrorList) -> list:
    import aws_sdk_sagemaker.types.batch_add_cluster_nodes_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.batch_add_cluster_nodes_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchAddClusterNodesErrorList:
    import aws_sdk_sagemaker.types.batch_add_cluster_nodes_error

    out: BatchAddClusterNodesErrorList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.batch_add_cluster_nodes_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
