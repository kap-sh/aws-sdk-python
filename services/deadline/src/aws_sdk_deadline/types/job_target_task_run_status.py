"""Generated from Smithy shape ``com.amazonaws.deadline#JobTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

JobTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JobTargetTaskRunStatus:
    return cast(JobTargetTaskRunStatus, data)
