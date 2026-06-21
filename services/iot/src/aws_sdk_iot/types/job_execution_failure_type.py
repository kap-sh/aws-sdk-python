"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionFailureType``."""

from typing import Literal, TypeAlias, cast

JobExecutionFailureType: TypeAlias = Literal[
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionFailureType) -> str:
    return value


def deserialize_json(data: str) -> JobExecutionFailureType:
    return cast(JobExecutionFailureType, data)
