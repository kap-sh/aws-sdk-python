"""Generated from Smithy shape ``com.amazonaws.pcs#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
    "UPDATE_FAILED",
    "SUSPENDING",
    "SUSPENDED",
    "RESUMING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterStatus:
    return cast(ClusterStatus, data)
