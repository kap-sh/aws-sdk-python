"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobsQueryStatus``."""

from typing import Literal, TypeAlias, cast

"""A job query's status can be SUBMITTED, PROGRESSING, COMPLETE, or ERROR."""
JobsQueryStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PROGRESSING",
    "COMPLETE",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobsQueryStatus) -> str:
    return value


def deserialize_json(data: str) -> JobsQueryStatus:
    return cast(JobsQueryStatus, data)
