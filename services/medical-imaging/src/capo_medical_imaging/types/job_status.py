"""Generated from Smithy shape ``com.amazonaws.medicalimaging#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
