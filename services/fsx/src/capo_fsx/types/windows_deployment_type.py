"""Generated from Smithy shape ``com.amazonaws.fsx#WindowsDeploymentType``."""

from typing import Literal, TypeAlias, cast

WindowsDeploymentType: TypeAlias = Literal[
    "MULTI_AZ_1",
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WindowsDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WindowsDeploymentType:
    return cast(WindowsDeploymentType, data)
