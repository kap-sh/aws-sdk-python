"""Generated from Smithy shape ``com.amazonaws.deadline#JobTargetTaskRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

JobTargetTaskRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "FAILED",
        "SUCCEEDED",
        "CANCELED",
        "SUSPENDED",
        "PENDING",
    )
)


def serialize_json(value: JobTargetTaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JobTargetTaskRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobTargetTaskRunStatus value: {data!r}")
    return cast(JobTargetTaskRunStatus, data)
