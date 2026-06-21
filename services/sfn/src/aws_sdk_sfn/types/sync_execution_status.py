"""Generated from Smithy shape ``com.amazonaws.sfn#SyncExecutionStatus``."""

from typing import Literal, TypeAlias, cast

SyncExecutionStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SyncExecutionStatus:
    return cast(SyncExecutionStatus, data)
