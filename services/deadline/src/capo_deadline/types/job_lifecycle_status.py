"""Generated from Smithy shape ``com.amazonaws.deadline#JobLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

JobLifecycleStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "CREATE_COMPLETE",
    "UPLOAD_IN_PROGRESS",
    "UPLOAD_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_SUCCEEDED",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> JobLifecycleStatus:
    return cast(JobLifecycleStatus, data)
