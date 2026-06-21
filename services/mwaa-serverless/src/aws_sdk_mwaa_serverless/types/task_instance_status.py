"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TaskInstanceStatus``."""

from typing import Literal, TypeAlias, cast

TaskInstanceStatus: TypeAlias = Literal[
    "QUEUED",
    "FAILED",
    "SCHEDULED",
    "RUNNING",
    "SUCCESS",
    "UP_FOR_RESCHEDULE",
    "UP_FOR_RETRY",
    "UPSTREAM_FAILED",
    "REMOVED",
    "RESTARTING",
    "DEFERRED",
    "NONE",
    "CANCELLED",
    "TIMEOUT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TaskInstanceStatus:
    return cast(TaskInstanceStatus, data)
