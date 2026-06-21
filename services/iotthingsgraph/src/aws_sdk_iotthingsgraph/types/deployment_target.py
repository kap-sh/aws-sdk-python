"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#DeploymentTarget``."""

from typing import Literal, TypeAlias, cast

DeploymentTarget: TypeAlias = Literal[
    "GREENGRASS",
    "CLOUD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTarget) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeploymentTarget:
    return cast(DeploymentTarget, data)
