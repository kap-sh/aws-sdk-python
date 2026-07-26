"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobStatus``."""

from typing import Literal, TypeAlias, cast

"""A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR."""
JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PROGRESSING",
    "COMPLETE",
    "CANCELED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
