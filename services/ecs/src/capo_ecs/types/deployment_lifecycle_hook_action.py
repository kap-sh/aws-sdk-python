"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookAction``."""

from typing import Literal, TypeAlias, cast

DeploymentLifecycleHookAction: TypeAlias = Literal[
    "ROLLBACK",
    "CONTINUE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookAction:
    return cast(DeploymentLifecycleHookAction, data)
