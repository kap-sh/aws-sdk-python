"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunStatus``."""

from typing import Literal, TypeAlias, cast

JobRunStatus: TypeAlias = Literal[
    "SCHEDULED",
    "IN_PROGRESS",
    "SUCCESS",
    "PARTIALLY_SUCCEEDED",
    "FAILED",
    "ABORTED",
    "TIMED_OUT",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JobRunStatus:
    return cast(JobRunStatus, data)
