"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceDeploymentState``."""

from typing import Literal, TypeAlias, cast

ContainerServiceDeploymentState: TypeAlias = Literal[
    "ACTIVATING",
    "ACTIVE",
    "INACTIVE",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceDeploymentState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceDeploymentState:
    return cast(ContainerServiceDeploymentState, data)
