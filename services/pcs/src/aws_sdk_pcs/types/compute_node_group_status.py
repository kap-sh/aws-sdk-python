"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupStatus``."""

from typing import Literal, TypeAlias, cast

ComputeNodeGroupStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
    "UPDATE_FAILED",
    "DELETED",
    "SUSPENDING",
    "SUSPENDED",
    "RESUMING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeNodeGroupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeNodeGroupStatus:
    return cast(ComputeNodeGroupStatus, data)
