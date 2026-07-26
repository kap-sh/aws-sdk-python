"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoScalingMode``."""

from typing import Literal, TypeAlias, cast

ClusterAutoScalingMode: TypeAlias = Literal[
    "Enable",
    "Disable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoScalingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterAutoScalingMode:
    return cast(ClusterAutoScalingMode, data)
