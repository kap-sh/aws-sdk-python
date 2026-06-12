"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNodeLogicalIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_node_logical_id

ClusterNodeLogicalIdList: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_node_logical_id.ClusterNodeLogicalId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNodeLogicalIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClusterNodeLogicalIdList:
    return list(data)
