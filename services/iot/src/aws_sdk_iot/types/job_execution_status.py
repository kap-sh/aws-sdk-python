"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionStatus``."""

from typing import Literal, TypeAlias, cast

JobExecutionStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "REJECTED",
    "REMOVED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> JobExecutionStatus:
    return cast(JobExecutionStatus, data)
