"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

EdgePresetDeploymentStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePresetDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePresetDeploymentStatus:
    return cast(EdgePresetDeploymentStatus, data)
