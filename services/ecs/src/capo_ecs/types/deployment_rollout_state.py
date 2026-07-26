"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentRolloutState``."""

from typing import Literal, TypeAlias, cast

DeploymentRolloutState: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentRolloutState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentRolloutState:
    return cast(DeploymentRolloutState, data)
