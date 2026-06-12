"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceGroupsToDelete``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_instance_group_name

ClusterInstanceGroupsToDelete: TypeAlias = list[
    "aws_sdk_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceGroupsToDelete) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClusterInstanceGroupsToDelete:
    return list(data)
