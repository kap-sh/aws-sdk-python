"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookTargetType``."""

from typing import Literal, TypeAlias, cast

DeploymentLifecycleHookTargetType: TypeAlias = Literal[
    "AWS_LAMBDA",
    "PAUSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookTargetType:
    return cast(DeploymentLifecycleHookTargetType, data)
