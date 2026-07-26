"""Generated from Smithy shape ``com.amazonaws.pcs#QueueStatus``."""

from typing import Literal, TypeAlias, cast

QueueStatus: TypeAlias = Literal[
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
def serialize_aws_json_1_0(value: QueueStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> QueueStatus:
    return cast(QueueStatus, data)
