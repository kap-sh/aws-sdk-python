"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeploymentType``."""

from typing import Literal, TypeAlias, cast

DeploymentType: TypeAlias = Literal[
    "SINGLE_AZ",
    "WITH_MULTIAZ_STANDBY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeploymentType:
    return cast(DeploymentType, data)
