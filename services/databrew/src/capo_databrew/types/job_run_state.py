"""Generated from Smithy shape ``com.amazonaws.databrew#JobRunState``."""

from typing import Literal, TypeAlias, cast

JobRunState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunState) -> str:
    return value


def deserialize_json(data: str) -> JobRunState:
    return cast(JobRunState, data)
