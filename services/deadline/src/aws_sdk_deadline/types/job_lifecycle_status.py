"""Generated from Smithy shape ``com.amazonaws.deadline#JobLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_FAILED",
        "CREATE_COMPLETE",
        "UPLOAD_IN_PROGRESS",
        "UPLOAD_FAILED",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
        "UPDATE_SUCCEEDED",
        "ARCHIVED",
    )
)


def serialize_json(value: JobLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> JobLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobLifecycleStatus value: {data!r}")
    return cast(JobLifecycleStatus, data)
