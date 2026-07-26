"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentStatus``."""

from typing import Literal, TypeAlias, cast

EnvironmentStatus: TypeAlias = Literal[
    "error",
    "creating",
    "connecting",
    "ready",
    "stopping",
    "stopped",
    "deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentStatus:
    return cast(EnvironmentStatus, data)
