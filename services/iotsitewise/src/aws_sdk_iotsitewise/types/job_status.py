"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "PENDING",
    "CANCELLED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "COMPLETED_WITH_FAILURES",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
