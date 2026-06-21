"""Generated from Smithy shape ``com.amazonaws.cloud9#EnvironmentLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

EnvironmentLifecycleStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "CREATE_FAILED",
    "DELETING",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentLifecycleStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnvironmentLifecycleStatus:
    return cast(EnvironmentLifecycleStatus, data)
