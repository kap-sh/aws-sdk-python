"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchRebootClusterNodesErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.batch_reboot_cluster_nodes_error

BatchRebootClusterNodesErrors: TypeAlias = list[
    "capo_sagemaker.types.batch_reboot_cluster_nodes_error.BatchRebootClusterNodesError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRebootClusterNodesErrors) -> list:
    import capo_sagemaker.types.batch_reboot_cluster_nodes_error

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.batch_reboot_cluster_nodes_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchRebootClusterNodesErrors:
    import capo_sagemaker.types.batch_reboot_cluster_nodes_error

    out: BatchRebootClusterNodesErrors = []
    for item in data:
        out.append(
            capo_sagemaker.types.batch_reboot_cluster_nodes_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
