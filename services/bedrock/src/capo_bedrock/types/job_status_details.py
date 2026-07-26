"""Generated from Smithy shape ``com.amazonaws.bedrock#JobStatusDetails``."""

from typing import Literal, TypeAlias, cast

JobStatusDetails: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Stopping",
    "Stopped",
    "Failed",
    "NotStarted",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobStatusDetails) -> str:
    return value


def deserialize_json(data: str) -> JobStatusDetails:
    return cast(JobStatusDetails, data)
