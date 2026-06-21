"""Generated from Smithy shape ``com.amazonaws.s3tables#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "Not_Yet_Run",
    "Successful",
    "Failed",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
