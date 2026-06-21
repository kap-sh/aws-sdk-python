"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "PENDING_CONCURRENCY",
    "PENDING_DEVICE",
    "PROCESSING",
    "SCHEDULING",
    "PREPARING",
    "RUNNING",
    "COMPLETED",
    "STOPPING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
