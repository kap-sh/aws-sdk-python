"""Generated from Smithy shape ``com.amazonaws.evs#HostState``."""

from typing import Literal, TypeAlias, cast

HostState: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "UPDATING",
    "DELETING",
    "DELETED",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HostState:
    return cast(HostState, data)
