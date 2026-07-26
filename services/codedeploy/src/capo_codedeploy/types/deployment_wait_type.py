"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentWaitType``."""

from typing import Literal, TypeAlias, cast

DeploymentWaitType: TypeAlias = Literal[
    "READY_WAIT",
    "TERMINATION_WAIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentWaitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentWaitType:
    return cast(DeploymentWaitType, data)
