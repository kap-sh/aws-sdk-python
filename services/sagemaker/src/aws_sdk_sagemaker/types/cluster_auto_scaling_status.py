"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingStatus``."""

from typing import Literal, TypeAlias, cast

ClusterAutoScalingStatus: TypeAlias = Literal[
    "InService",
    "Failed",
    "Creating",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalingStatus:
    return cast(ClusterAutoScalingStatus, data)
