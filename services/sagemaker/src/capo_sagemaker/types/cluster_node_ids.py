"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_node_id

ClusterNodeIds: TypeAlias = list["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClusterNodeIds:
    return list(data)
