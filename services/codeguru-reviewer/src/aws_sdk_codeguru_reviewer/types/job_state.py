"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#JobState``."""

from typing import Literal, TypeAlias, cast

JobState: TypeAlias = Literal[
    "Completed",
    "Pending",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobState) -> str:
    return value


def deserialize_json(data: str) -> JobState:
    return cast(JobState, data)
