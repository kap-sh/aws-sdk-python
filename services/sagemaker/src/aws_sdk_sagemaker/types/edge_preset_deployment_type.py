"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgePresetDeploymentType``."""

from typing import Literal, TypeAlias, cast

EdgePresetDeploymentType: TypeAlias = Literal["GreengrassV2Component",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgePresetDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EdgePresetDeploymentType:
    return cast(EdgePresetDeploymentType, data)
