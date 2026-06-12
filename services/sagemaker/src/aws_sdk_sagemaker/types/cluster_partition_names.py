"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterPartitionNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_partition_name

ClusterPartitionNames: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_partition_name.ClusterPartitionName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPartitionNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClusterPartitionNames:
    return list(data)
