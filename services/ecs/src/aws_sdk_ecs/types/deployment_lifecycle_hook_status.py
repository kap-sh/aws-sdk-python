"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentLifecycleHookStatus``."""

from typing import Literal, TypeAlias, cast

DeploymentLifecycleHookStatus: TypeAlias = Literal[
    "AWAITING_ACTION",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentLifecycleHookStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentLifecycleHookStatus:
    return cast(DeploymentLifecycleHookStatus, data)
