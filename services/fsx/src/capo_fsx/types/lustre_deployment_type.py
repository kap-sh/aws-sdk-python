"""Generated from Smithy shape ``com.amazonaws.fsx#LustreDeploymentType``."""

from typing import Literal, TypeAlias, cast

LustreDeploymentType: TypeAlias = Literal[
    "SCRATCH_1",
    "SCRATCH_2",
    "PERSISTENT_1",
    "PERSISTENT_2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LustreDeploymentType:
    return cast(LustreDeploymentType, data)
