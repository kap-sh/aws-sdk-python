"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSDeploymentType``."""

from typing import Literal, TypeAlias, cast

OpenZFSDeploymentType: TypeAlias = Literal[
    "SINGLE_AZ_1",
    "SINGLE_AZ_2",
    "SINGLE_AZ_HA_1",
    "SINGLE_AZ_HA_2",
    "MULTI_AZ_1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSDeploymentType:
    return cast(OpenZFSDeploymentType, data)
