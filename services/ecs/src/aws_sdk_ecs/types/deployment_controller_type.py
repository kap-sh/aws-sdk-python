"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentControllerType``."""

from typing import Literal, TypeAlias, cast

DeploymentControllerType: TypeAlias = Literal[
    "ECS",
    "CODE_DEPLOY",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentControllerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentControllerType:
    return cast(DeploymentControllerType, data)
