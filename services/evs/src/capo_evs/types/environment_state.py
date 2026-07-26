"""Generated from Smithy shape ``com.amazonaws.evs#EnvironmentState``."""

from typing import Literal, TypeAlias, cast

EnvironmentState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnvironmentState:
    return cast(EnvironmentState, data)
