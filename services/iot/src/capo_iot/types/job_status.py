"""Generated from Smithy shape ``com.amazonaws.iot#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "COMPLETED",
    "DELETION_IN_PROGRESS",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
