"""Generated from Smithy shape ``com.amazonaws.amplify#JobStatus``."""

from typing import Literal, TypeAlias, cast

JobStatus: TypeAlias = Literal[
    "CREATED",
    "PENDING",
    "PROVISIONING",
    "RUNNING",
    "FAILED",
    "SUCCEED",
    "CANCELLING",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    return cast(JobStatus, data)
