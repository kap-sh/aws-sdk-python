"""Generated from Smithy shape ``com.amazonaws.macie2#JobStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a classification job. Possible values are:</p>"""
JobStatus: TypeAlias = Literal[
    "RUNNING",
    "PAUSED",
    "CANCELLED",
    "COMPLETE",
    "IDLE",
    "USER_PAUSED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
