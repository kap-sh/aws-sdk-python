"""Generated from Smithy shape ``com.amazonaws.pinpoint#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "CREATED",
    "PREPARING_FOR_INITIALIZATION",
    "INITIALIZING",
    "PROCESSING",
    "PENDING_JOB",
    "COMPLETING",
    "COMPLETED",
    "FAILING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
