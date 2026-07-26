"""Generated from Smithy shape ``com.amazonaws.ecs#DeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

DeploymentStrategy: TypeAlias = Literal[
    "ROLLING",
    "BLUE_GREEN",
    "LINEAR",
    "CANARY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentStrategy:
    return cast(DeploymentStrategy, data)
