"""Generated from Smithy shape ``com.amazonaws.deadline#CreateJobTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

CreateJobTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "SUSPENDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> CreateJobTargetTaskRunStatus:
    return cast(CreateJobTargetTaskRunStatus, data)
