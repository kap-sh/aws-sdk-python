"""Generated from Smithy shape ``com.amazonaws.emrcontainers#JobRunState``."""

from typing import Literal, TypeAlias, cast

JobRunState: TypeAlias = Literal[
    "PENDING",
    "SUBMITTED",
    "RUNNING",
    "FAILED",
    "CANCELLED",
    "CANCEL_PENDING",
    "COMPLETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunState) -> str:
    return value


def deserialize_json(data: str) -> JobRunState:
    return cast(JobRunState, data)
