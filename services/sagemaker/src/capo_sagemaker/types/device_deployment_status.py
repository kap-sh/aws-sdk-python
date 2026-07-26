"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

DeviceDeploymentStatus: TypeAlias = Literal[
    "READYTODEPLOY",
    "INPROGRESS",
    "DEPLOYED",
    "FAILED",
    "STOPPING",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceDeploymentStatus:
    return cast(DeviceDeploymentStatus, data)
